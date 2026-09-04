import { motion, useReducedMotion } from 'framer-motion'
import { useEffect, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import { fetchTeamMembers } from '../services/api'
import './EditorialPages.css'

function Team() {
  const shouldReduceMotion = useReducedMotion()
  const [members, setMembers] = useState(null)
  const [error, setError] = useState(false)

  useEffect(() => {
    let isCurrent = true
    fetchTeamMembers()
      .then((response) => {
        if (!isCurrent) return
        setError(false)
        setMembers(Array.isArray(response) ? response : response.results || [])
      })
      .catch(() => isCurrent && setError(true))
    return () => { isCurrent = false }
  }, [])

  if (!members && !error) return <LoadingState />

  return (
    <div className="editorial-page">
      <Seo
        title="Team"
        description="Meet the public-facing executive committee of Alliance Yuwa Club, the youth-led community organization formed through the First General Convention in Biratnagar."
        path="/team"
      />
      <header className="page-container editorial-intro">
        <p className="content-eyebrow">Executive committee</p>
        <h1>People behind the work.</h1>
        <p>Meet the public-facing executive committee formed through the First General Convention / Adhibheshana.</p>
      </header>
      <section className="page-container team-section" aria-labelledby="team-title">
        <h2 id="team-title" className="sr-only">Alliance Yuwa Club executive committee</h2>
        {error ? <div className="content-message" role="alert">Unable to load the executive committee right now. Please try again shortly.</div>
          : members.length === 0 ? <div className="content-message">Executive committee information will be published after it is verified by the club.</div>
          : <div className="team-grid">
            {members.map((member, index) => (
              <motion.article
                key={member.id}
                className="team-member"
                initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: shouldReduceMotion ? 0 : 0.35, delay: shouldReduceMotion ? 0 : index * 0.04 }}
                whileHover={shouldReduceMotion ? {} : { y: -4 }}
              >
                <MediaFrame className="team-member__photo" src={member.photo} alt={`${member.name} profile photograph`} label="Executive member portrait" />
                <div className="team-member__body">
                  <p>{member.position}</p>
                  <h3>{member.name}</h3>
                  {member.bio && <p className="team-member__bio">{member.bio}</p>}
                  <span className="team-member__social">Verified social links will be added when published.</span>
                </div>
              </motion.article>
            ))}
          </div>}
      </section>
    </div>
  )
}

export default Team
