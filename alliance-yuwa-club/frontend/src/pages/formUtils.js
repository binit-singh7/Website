export function required(value, message) {
  return String(value || '').trim() ? '' : message
}

export function isValidEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
}

export function isValidPhone(value) {
  return /^\+?[0-9][0-9\s-]{6,28}$/.test(value)
}

export function getSubmissionErrors(error) {
  const responseErrors = error?.response?.data
  if (responseErrors && typeof responseErrors === 'object') {
    return Object.fromEntries(
      Object.entries(responseErrors)
        .filter(([field]) => field !== 'detail' && field !== 'message')
        .map(([field, messages]) => [field, Array.isArray(messages) ? messages[0] : String(messages)]),
    )
  }

  return {}
}

export function getSubmissionMessage(error, fallback) {
  const detail = error?.response?.data?.detail || error?.response?.data?.message
  return typeof detail === 'string' ? detail : fallback
}
