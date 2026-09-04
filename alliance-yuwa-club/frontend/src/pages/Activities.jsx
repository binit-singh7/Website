import { motion, useReducedMotion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import { fetchActivities } from '../services/api'
import { collectionResult, excerpt, formatDate } from './contentUtils'
import './ContentPages.css'

const categoryFilters = [
  ['All', ''],
  ['Community', 'community-service'],
  ['Environment', 'environment'],
  ['Youth', 'youth-leadership'],
  ['Sports', 'sports'],
  ['Culture', 'culture'],
  ['Awareness', 'awareness'],
  ['Health', 'health'],
]
const years = [2026, 2025, 2024, 2023, 2022, 2021, 2020]

function Activities() {
  const shouldReduceMotion = useReducedMotion()
  const [category, setCategory] = useState('')
  const [year, setYear] = useState(2026)
  const [page, setPage] = useState(1)
  const [data, setData] = useState(null)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true

    fetchActivities({ category, year, page, pageSize: 12 })
      .then((response) => {
        if (!isCurrent) return
        setError(false)
        setData(collectionResult(response))
      })
      .catch(() => isCurrent && setError(true))

    return () => { isCurrent = false }
  }, [category, page, year])

  function selectCategory(nextCategory) {
    setCategory(nextCategory)
    setPage(1)
  }

  function selectYear(nextYear) {
    setYear(nextYear)
    setPage(1)
  }

  if (!data && !error) return <LoadingState />

  return (
    <div className="content-page">
      <Seo
        title="Activities"
        description="Explore published records of Alliance Yuwa Club community action, youth leadership, environment, culture, sport, and service in Biratnagar from 2020 to today."
        path="/activities"
      />
      <header className="content-intro page-container">
        <p className="content-eyebrow">Activity archive · 2020–2026</p>
        <h1>Our work, year by year.</h1>
        <p>Explore published records of community action, youth leadership, and service from Alliance Yuwa Club.</p>
      </header>

      <section className="page-container content-controls" aria-label="Activity archive filters">
        <div className="filter-group">
          <p id="category-filter-label">Filter by category</p>
          <div aria-labelledby="category-filter-label" className="filter-bar" role="toolbar">
            {categoryFilters.map(([label, value]) => (
              <button
                key={value || 'all'}
                type="button"
                aria-pressed={category === value}
                className={category === value ? 'filter-button filter-button--active' : 'filter-button'}
                onClick={() => selectCategory(value)}
              >
                {label}
              </button>
            ))}
          </div>
        </div>
        <div className="filter-group">
          <p id="year-filter-label">Activity timeline</p>
          <div aria-labelledby="year-filter-label" className="year-bar" role="toolbar">
            {years.map((timelineYear) => (
              <button
                key={timelineYear}
                type="button"
                aria-pressed={year === timelineYear}
                className={year === timelineYear ? 'year-button year-button--active' : 'year-button'}
                onClick={() => selectYear(timelineYear)}
              >
                {timelineYear}
              </button>
            ))}
          </div>
        </div>
      </section>

      <section className="page-container content-results" aria-labelledby="activity-results-title">
        <div className="content-results__heading">
          <p className="content-eyebrow">{year}</p>
          <h2 id="activity-results-title">Published activity records</h2>
        </div>
        {error ? (
          <div className="content-message" role="alert">Unable to load activities right now. Please try again shortly.</div>
        ) : data.results.length === 0 ? (
          <div className="content-message">No published activities match these filters yet.</div>
        ) : (
          <div className="record-grid">
            {data.results.map((activity, index) => (
              <motion.article
                key={activity.id}
                className="record-card"
                initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: shouldReduceMotion ? 0 : 0.35, delay: shouldReduceMotion ? 0 : index * 0.04 }}
                whileHover={shouldReduceMotion ? {} : { y: -4 }}
              >
                <Link to={`/activities/${activity.slug}`}>
                  <MediaFrame className="record-card__media" src={activity.cover_image} alt={`${activity.title} cover image`} label="Activity photograph" />
                  <div className="record-card__body">
                    <p className="record-card__category">{activity.category?.name || 'Activity'}</p>
                    <p className="record-card__meta">{formatDate(activity.date)}{activity.location && <> <span aria-hidden="true">·</span> {activity.location}</>}</p>
                    <h3>{activity.title}</h3>
                    <p>{excerpt(activity.description)}</p>
                    <span className="record-card__link">Read record <span aria-hidden="true">→</span></span>
                  </div>
                </Link>
              </motion.article>
            ))}
          </div>
        )}
        {data && data.count > data.results.length && (
          <nav className="content-pagination" aria-label="Activity archive pages">
            <button type="button" disabled={!data.previous} onClick={() => setPage((current) => current - 1)}>Previous</button>
            <span>Page {page}</span>
            <button type="button" disabled={!data.next} onClick={() => setPage((current) => current + 1)}>Next</button>
          </nav>
        )}
      </section>
    </div>
  )
}

export default Activities
