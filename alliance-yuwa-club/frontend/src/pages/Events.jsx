import { motion, useReducedMotion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import { fetchEvents } from '../services/api'
import { collectionResult, excerpt, formatDateTime } from './contentUtils'
import './ContentPages.css'

const statusLabels = {
  upcoming: 'Upcoming',
  ongoing: 'Ongoing',
  completed: 'Completed',
  cancelled: 'Cancelled',
}

function Events() {
  const shouldReduceMotion = useReducedMotion()
  const [data, setData] = useState(null)
  const [page, setPage] = useState(1)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true

    fetchEvents({ page, pageSize: 12 })
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
    <div className="content-page">
      <Seo
        title="Events"
        description="Find published Alliance Yuwa Club events in Biratnagar, from upcoming community programs and gatherings to completed milestones."
        path="/events"
      />
      <header className="content-intro page-container">
        <p className="content-eyebrow">Events</p>
        <h1>Gather. Serve. Lead.</h1>
        <p>Find published Alliance Yuwa Club events, from upcoming community programs to completed milestones.</p>
      </header>
      <section className="page-container event-results" aria-labelledby="event-results-title">
        <div className="content-results__heading">
          <p className="content-eyebrow">Scheduled events</p>
          <h2 id="event-results-title">What’s happening</h2>
        </div>
        {error ? (
          <div className="content-message" role="alert">Unable to load events right now. Please try again shortly.</div>
        ) : data.results.length === 0 ? (
          <div className="content-message">No public events are available at the moment. Please check back soon.</div>
        ) : (
          <div className="event-list">
            {data.results.map((event, index) => (
              <motion.article
                key={event.id}
                className="event-record"
                initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: shouldReduceMotion ? 0 : 0.35, delay: shouldReduceMotion ? 0 : index * 0.04 }}
                whileHover={shouldReduceMotion ? {} : { y: -4 }}
              >
                <Link to={`/events/${event.slug}`}>
                  <MediaFrame className="event-record__media" src={event.cover_image} alt={`${event.title} cover image`} label="Event photograph" />
                  <div className="event-record__body">
                    <div className="event-record__topline">
                      <span className={`event-status event-status--${event.status}`}>{statusLabels[event.status] || event.status}</span>
                      <p>{formatDateTime(event.start_datetime)}</p>
                    </div>
                    <h3>{event.title}</h3>
                    <p className="event-record__location">{event.location || 'Location to be confirmed'}</p>
                    <p>{excerpt(event.description)}</p>
                    <span className="record-card__link">View event <span aria-hidden="true">→</span></span>
                  </div>
                </Link>
              </motion.article>
            ))}
          </div>
        )}
        {data && data.count > data.results.length && (
          <nav className="content-pagination" aria-label="Event pages">
            <button type="button" disabled={!data.previous} onClick={() => setPage((current) => current - 1)}>Previous</button>
            <span>Page {page}</span>
            <button type="button" disabled={!data.next} onClick={() => setPage((current) => current + 1)}>Next</button>
          </nav>
        )}
      </section>
    </div>
  )
}

export default Events
