export function formatDate(date) {
  if (!date) return 'Date to be announced'

  return new Intl.DateTimeFormat('en', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  }).format(new Date(`${date}T00:00:00`))
}

export function formatDateTime(dateTime) {
  if (!dateTime) return 'Date to be announced'

  return new Intl.DateTimeFormat('en', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  }).format(new Date(dateTime))
}

export function excerpt(text, length = 165) {
  if (!text) return 'A published activity record will appear here.'
  return text.length > length ? `${text.slice(0, length).trimEnd()}…` : text
}

export function collectionResult(data) {
  return Array.isArray(data)
    ? { count: data.length, next: null, previous: null, results: data }
    : data
}
