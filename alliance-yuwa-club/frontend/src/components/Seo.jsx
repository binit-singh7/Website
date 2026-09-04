import { Helmet } from 'react-helmet-async'

const SITE_NAME = 'Alliance Yuwa Club'
// Canonical production origin for SEO URLs. Overridable via VITE_SITE_URL so
// staging/preview deployments can point canonical tags at the right host.
const SITE_URL = (import.meta.env.VITE_SITE_URL || 'https://allianceyuwaclub.org.np').replace(/\/+$/, '')

function absoluteUrl(path = '/') {
  if (/^https?:\/\//i.test(path)) return path
  return `${SITE_URL}/${String(path).replace(/^\/+/, '')}`
}

/**
 * Reusable SEO head metadata for a route. Renders only react-helmet-async
 * tags (title, meta description, Open Graph, Twitter, canonical) and adds no
 * visible DOM, so it never affects page layout or styling.
 */
export default function Seo({ title, description, path = '/', type = 'website' }) {
  const fullTitle = title ? `${title} | ${SITE_NAME}` : `${SITE_NAME} | Unity. Leadership. Service.`
  const canonical = absoluteUrl(path)

  return (
    <Helmet>
      <title>{fullTitle}</title>
      <meta name="description" content={description} />
      <link rel="canonical" href={canonical} />
      <meta property="og:type" content={type} />
      <meta property="og:site_name" content={SITE_NAME} />
      <meta property="og:title" content={fullTitle} />
      <meta property="og:description" content={description} />
      <meta property="og:url" content={canonical} />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={fullTitle} />
      <meta name="twitter:description" content={description} />
    </Helmet>
  )
}