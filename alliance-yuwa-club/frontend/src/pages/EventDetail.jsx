import { motion, useReducedMotion } from 'framer-motion'
import { Link, useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import { fetchEvent } from '../services/api'
import { formatDateTime } from './contentUtils'
import './ContentPages.css'

const statusLabels = {
  upcoming: 'Upcoming',
  ongoing: 'Ongoing',
  completed: 'Completed',
  cancelled: 'Cancelled',
}

function EventDetail() {
  const { slug } = useParams()
  const shouldReduceMotion = useReducedMotion()
  const [event, setEvent] = useState(null)
  const [notFound, setNotFound] = useState(false)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true

    fetchEvent(slug)
      .then((response) => {
        if (!isCurrent) return
        setNotFound(false)
        setError(false)
        setEvent(response)
      })
      .catch((requestError) => {
        if (!isCurrent) return
        setEvent(null)
        setNotFound(requestError.response?.status === 404)
        setError(requestError.response?.status !== 404)
      })

    return () => { isCurrent = false }
  }, [slug])

  if (!event && !notFound && !error) return <LoadingState />

  if (notFound || error) {
    return (
      <div className="page-container content-detail-message" role={error ? 'alert' : undefined}>
        <Seo
          title="Event unavailable"
          description="This event is not available. Browse the published Alliance Yuwa Club events list instead."
          path={`/events/${slug}`}
          robots="noindex, follow"
        />
        <p className="content-eyebrow">Events</p>
        <h1>{notFound ? 'This event is not available.' : 'We could not load this event.'}</h1>
        <p>Return to the events list to continue exploring the club’s public schedule.</p>
        <Link className="text-link" to="/events">Back to events</Link>
      </div>
    )
  }

  return (
    <article className="content-detail">
      <Seo
        title={event.title}
        description={event.description}
        path={`/events/${event.slug}`}
        type="article"
        image={event.cover_image}
      />
      <motion.header
        className="page-container detail-hero"
        initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 18 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: shouldReduceMotion ? 0 : 0.45 }}
      >
        <Link className="text-link" to="/events">← Back to events</Link>
        <p className="content-eyebrow"><span className={`event-status event-status--${event.status}`}>{statusLabels[event.status] || event.status}</span></p>
        <h1>{event.title}</h1>
        <dl className="detail-facts">
          <div><dt>Starts</dt><dd>{formatDateTime(event.start_datetime)}</dd></div>
          <div><dt>Ends</dt><dd>{event.end_datetime ? formatDateTime(event.end_datetime) : 'To be announced'}</dd></div>
          <div><dt>Location</dt><dd>{event.location || 'Location to be confirmed'}</dd></div>
        </dl>
      </motion.header>
      <div className="page-container detail-layout">
        <MediaFrame className="detail-cover" src={event.cover_image} alt={`${event.title} cover image`} label="Event cover photograph" />
        <div className="detail-copy">
          <section aria-labelledby="event-description-title">
            <h2 id="event-description-title">About this event</h2>
            <p>{event.description}</p>
          </section>
          {event.registration_required && (
            <section aria-labelledby="event-registration-title">
              <h2 id="event-registration-title">Registration</h2>
              {event.registration_url ? <a className="text-link" href={event.registration_url}>Register for this event</a> : <p>Registration details will be announced by the club.</p>}
            </section>
          )}
        </div>
      </div>
      <section className="page-container detail-gallery" aria-labelledby="event-gallery-title">
        <div className="content-results__heading">
          <p className="content-eyebrow">Event gallery</p>
          <h2 id="event-gallery-title">Images from the event</h2>
        </div>
        {event.images?.length ? (
          <div className="gallery-grid">
            {event.images.map((image) => <MediaFrame key={image.id} className="gallery-grid__image" src={image.image} alt={image.caption || `${event.title} event photograph`} label="Event photograph" />)}
          </div>
        ) : <div className="content-message">No event images have been published yet.</div>}
      </section>
    </article>
  )
}

export default EventDetail
