import { motion, useReducedMotion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import { fetchNews } from '../services/api'
import { collectionResult, excerpt, formatDateTime } from './contentUtils'
import './EditorialPages.css'

function readingEstimate(text) {
  const words = text?.trim().split(/\s+/).filter(Boolean).length || 0
  return `${Math.max(1, Math.ceil(words / 200))} min read`
}

function News() {
  const shouldReduceMotion = useReducedMotion()
  const [data, setData] = useState(null)
  const [page, setPage] = useState(1)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true
    fetchNews({ page, pageSize: 12 })
      .then((response) => {
        if (!isCurrent) return
        setError(false)
        setData(collectionResult(response))
      })
      .catch(() => isCurrent && setError(true))
    return () => { isCurrent = false }
  }, [page])

  if (!data && !error) return <LoadingState />

  return (
    <div className="editorial-page">
      <header className="page-container editorial-intro">
        <p className="content-eyebrow">News & updates</p>
        <h1>From the club.</h1>
        <p>Published reports, announcements, and updates from Alliance Yuwa Club.</p>
      </header>
      <section className="page-container news-section" aria-labelledby="news-title">
        <h2 id="news-title" className="sr-only">Published news articles</h2>
        {error ? <div className="content-message" role="alert">Unable to load news right now. Please try again shortly.</div>
          : data.results.length === 0 ? <div className="content-message">No published news is available at the moment. Please check back soon.</div>
          : <div className="news-grid">
            {data.results.map((article, index) => (
              <motion.article
                key={article.id}
                className="news-card"
                initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: shouldReduceMotion ? 0 : 0.35, delay: shouldReduceMotion ? 0 : index * 0.04 }}
                whileHover={shouldReduceMotion ? {} : { y: -4 }}
              >
                <Link to={`/news/${article.slug}`}>
                  <MediaFrame className="news-card__media" src={article.featured_image} alt={`${article.title} article image`} label="News article image" />
                  <div className="news-card__body">
                    <div className="news-card__meta"><span>Official update</span><time dateTime={article.published_at || undefined}>{formatDateTime(article.published_at)}</time></div>
                    <h3>{article.title}</h3>
                    <p>{excerpt(article.excerpt || article.title)}</p>
                    <span className="news-card__read">{readingEstimate(article.excerpt)} <span aria-hidden="true">·</span> Read article <span aria-hidden="true">→</span></span>
                  </div>
                </Link>
              </motion.article>
            ))}
          </div>}
        {data && data.count > data.results.length && (
          <nav className="content-pagination" aria-label="News pages">
            <button type="button" disabled={!data.previous} onClick={() => setPage((current) => current - 1)}>Previous</button>
            <span>Page {page}</span>
            <button type="button" disabled={!data.next} onClick={() => setPage((current) => current + 1)}>Next</button>
          </nav>
        )}
      </section>
    </div>
  )
}

export default News
