import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api',
  headers: { Accept: 'application/json' },
})

function requestCollection(path, params) {
  return api.get(path, { params }).then((response) => response.data)
}

export function fetchActivityCategories() {
  return requestCollection('/activity-categories/')
}

export function fetchActivities({ category, year, page, pageSize } = {}) {
  return requestCollection('/activities/', {
    category: category || undefined,
    year: year || undefined,
    page: page || undefined,
    page_size: pageSize || undefined,
  })
}

export function fetchActivity(slug) {
  return api.get(`/activities/${slug}/`).then((response) => response.data)
}

export function fetchEvents({ status, year, page, pageSize } = {}) {
  return requestCollection('/events/', {
    status: status || undefined,
    year: year || undefined,
    page: page || undefined,
    page_size: pageSize || undefined,
  })
}

export function fetchEvent(slug) {
  return api.get(`/events/${slug}/`).then((response) => response.data)
}

export function fetchNews({ year, page, pageSize } = {}) {
  return requestCollection('/news/', {
    year: year || undefined,
    page: page || undefined,
    page_size: pageSize || undefined,
  })
}

export function fetchNewsArticle(slug) {
  return api.get(`/news/${slug}/`).then((response) => response.data)
}

export function fetchTeamMembers() {
  return requestCollection('/team/')
}

export function fetchOrganization() {
  return api.get('/organization/').then((response) => response.data)
}

export function submitMembershipApplication(application) {
  return api.post('/membership/apply/', application).then((response) => response.data)
}

export function submitContactMessage(message) {
  return api.post('/contact/', message).then((response) => response.data)
}

export function mediaUrl(path) {
  return path ? new URL(path, api.defaults.baseURL).href : null
}

export default api
