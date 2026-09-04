import { motion, useReducedMotion } from 'framer-motion'
import { Link, useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import { fetchActivity } from '../services/api'
import { formatDate } from './contentUtils'
import './ContentPages.css'

function ActivityDetail() {
  const { slug } = useParams()
  const shouldReduceMotion = useReducedMotion()
  const [activity, setActivity] = useState(null)
  const [notFound, setNotFound] = useState(false)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true

    fetchActivity(slug)
      .then((response) => {
        if (!isCurrent) return
        setNotFound(false)
        setError(false)
        setActivity(response)
      })
      .catch((requestError) => {
        if (!isCurrent) return
        setActivity(null)
        setNotFound(requestError.response?.status === 404)
        setError(requestError.response?.status !== 404)
      })

    return () => { isCurrent = false }
  }, [slug])

  if (!activity && !notFound && !error) return <LoadingState />

  if (notFound || error) {
    return (
      <div className="page-container content-detail-message" role={error ? 'alert' : undefined}>
        <Seo
          title="Activity unavailable"
          description="This activity record is not available. Browse the published Alliance Yuwa Club activity archive instead."
          path={`/activities/${slug}`}
          robots="noindex, follow"
        />
        <p className="content-eyebrow">Activity archive</p>
        <h1>{notFound ? 'This activity is not available.' : 'We could not load this activity.'}</h1>
        <p>Return to the published activity archive to continue exploring the club’s work.</p>
        <Link className="text-link" to="/activities">Back to activities</Link>
      </div>
    )
  }

  return (
    <article className="content-detail">
      <Seo
        title={activity.title}
        description={activity.description}
        path={`/activities/${slug}`}
        type="article"
        image={activity.cover_image}
      />
      <motion.header
        className="page-container detail-hero"
        initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 18 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: shouldReduceMotion ? 0 : 0.45 }}
      >
        <Link className="text-link" to="/activities">← Back to activities</Link>
        <p className="content-eyebrow">{activity.category?.name || 'Activity'}</p>
        <h1>{activity.title}</h1>
        <dl className="detail-facts">
          <div><dt>Date</dt><dd>{formatDate(activity.date)}</dd></div>
          <div><dt>Location</dt><dd>{activity.location || 'Location to be confirmed'}</dd></div>
        </dl>
      </motion.header>
      <div className="page-container detail-layout">
        <MediaFrame className="detail-cover" src={activity.cover_image} alt={`${activity.title} cover image`} label="Activity cover photograph" />
        <div className="detail-copy">
          <section aria-labelledby="activity-description-title">
            <h2 id="activity-description-title">About this activity</h2>
            <p>{activity.description}</p>
          </section>
          <section aria-labelledby="activity-partners-title">
            <h2 id="activity-partners-title">Partners & organizers</h2>
            <p>Partner and organizer information is not yet listed in this public activity record.</p>
          </section>
        </div>
      </div>
      <section className="page-container detail-gallery" aria-labelledby="activity-gallery-title">
        <div className="content-results__heading">
          <p className="content-eyebrow">Activity gallery</p>
          <h2 id="activity-gallery-title">Images from the work</h2>
        </div>
        {activity.images?.length ? (
          <div className="gallery-grid">
            {activity.images.map((image) => <MediaFrame key={image.id} className="gallery-grid__image" src={image.image} alt={image.caption || `${activity.title} activity photograph`} label="Activity photograph" />)}
          </div>
        ) : <div className="content-message">No activity images have been published yet.</div>}
      </section>
    </article>
  )
}

export default ActivityDetail
