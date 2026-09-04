import { motion, useReducedMotion } from 'framer-motion'
import { Link, useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import { fetchNewsArticle } from '../services/api'
import { formatDateTime } from './contentUtils'
import './EditorialPages.css'

function readingEstimate(text) {
  const words = text?.trim().split(/\s+/).filter(Boolean).length || 0
  return `${Math.max(1, Math.ceil(words / 200))} min read`
}

function NewsDetail() {
  const { slug } = useParams()
  const shouldReduceMotion = useReducedMotion()
  const [article, setArticle] = useState(null)
  const [notFound, setNotFound] = useState(false)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true
    fetchNewsArticle(slug)
      .then((response) => {
        if (!isCurrent) return
        setNotFound(false)
        setError(false)
        setArticle(response)
      })
      .catch((requestError) => {
        if (!isCurrent) return
        setArticle(null)
        setNotFound(requestError.response?.status === 404)
        setError(requestError.response?.status !== 404)
      })
    return () => { isCurrent = false }
  }, [slug])

  if (!article && !notFound && !error) return <LoadingState />

  if (notFound || error) {
    return (
      <div className="page-container content-detail-message" role={error ? 'alert' : undefined}>
        <Seo
          title="Article unavailable"
          description="This news article is not available. Browse the published Alliance Yuwa Club news archive instead."
          path={`/news/${slug}`}
          robots="noindex, follow"
        />
        <p className="content-eyebrow">News & updates</p>
        <h1>{notFound ? 'This article is not available.' : 'We could not load this article.'}</h1>
        <p>Return to the news archive to continue reading published club updates.</p>
        <Link className="text-link" to="/news">Back to news</Link>
      </div>
    )
  }

  return (
    <article className="editorial-page news-detail">
      <Seo
        title={article.title}
        description={article.excerpt || article.content}
        path={`/news/${article.slug}`}
        type="article"
        image={article.featured_image}
      />
      <motion.header
        className="page-container news-detail__header"
        initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 18 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: shouldReduceMotion ? 0 : 0.45 }}
      >
        <Link className="text-link" to="/news">← Back to news</Link>
        <p className="content-eyebrow">Official update</p>
        <h1>{article.title}</h1>
        <p className="news-detail__meta"><time dateTime={article.published_at || undefined}>{formatDateTime(article.published_at)}</time> <span aria-hidden="true">·</span> {readingEstimate(article.content)}</p>
      </motion.header>
      <div className="page-container news-detail__media-wrap">
        <MediaFrame className="news-detail__media" src={article.featured_image} alt={`${article.title} article image`} label="News article image" />
      </div>
      <div className="page-container news-detail__content">
        <p className="news-detail__excerpt">{article.excerpt}</p>
        <div>{article.content}</div>
      </div>
    </article>
  )
}

export default NewsDetail
