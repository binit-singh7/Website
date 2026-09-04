import { Helmet } from 'react-helmet-async'

const SITE_NAME = 'Alliance Yuwa Club'
// Canonical production origin for SEO URLs. Overridable via VITE_SITE_URL so
// staging/preview deployments can point canonical tags at the right host.
const SITE_URL = (import.meta.env.VITE_SITE_URL || 'https://allianceyuwaclub.org.np').replace(/\/+$/, '')

function absoluteUrl(path = '/') {
  if (!path) return SITE_URL
  if (/^https?:\/\//i.test(path)) return path
  return `${SITE_URL}/${String(path).replace(/^\/+/, '')}`
}

// Collapse whitespace and keep meta descriptions within the recommended length.
function toDescription(value) {
  const text = String(value || '').replace(/\s+/g, ' ').trim()
  if (text.length <= 160) return text
  return `${text.slice(0, 157).trimEnd()}\u2026`
}

/**
 * Reusable SEO head metadata for a route. Renders only react-helmet-async tags
 * (title, meta description, robots, canonical, Open Graph, Twitter) and adds no
 * visible DOM, so it never affects page layout or styling. Detail pages pass
 * values derived from the fetched Django API record for dynamic metadata.
 */
export default function Seo({
  title,
  description,
  path = '/',
  type = 'website',
  image,
  robots = 'index, follow',
}) {
  const fullTitle = title ? `${title} | ${SITE_NAME}` : `${SITE_NAME} | Unity. Leadership. Service.`
  const canonical = absoluteUrl(path)
  const metaDescription = toDescription(description)
  // Only absolute image URLs (e.g. production Supabase media) are valid OG
  // images; relative /media/ paths would resolve against the wrong host, so
  // they are intentionally omitted.
  const ogImage = image && /^https?:\/\//i.test(image) ? image : null

  return (
    <Helmet>
      <title>{fullTitle}</title>
      <meta name="description" content={metaDescription} />
      <meta name="robots" content={robots} />
      <link rel="canonical" href={canonical} />
      <meta property="og:type" content={type} />
      <meta property="og:site_name" content={SITE_NAME} />
      <meta property="og:title" content={fullTitle} />
      <meta property="og:description" content={metaDescription} />
      <meta property="og:url" content={canonical} />
      {ogImage && <meta property="og:image" content={ogImage} />}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={fullTitle} />
      <meta name="twitter:description" content={metaDescription} />
      {ogImage && <meta name="twitter:image" content={ogImage} />}
    </Helmet>
  )
}