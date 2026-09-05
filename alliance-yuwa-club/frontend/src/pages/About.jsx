import { motion, useReducedMotion } from 'framer-motion'

import MediaFrame from '../components/MediaFrame'
import Seo from '../components/Seo'
import './EditorialPages.css'
import aboutImg from '../assets/club-photo.jpg'

const values = ['Unity', 'Leadership', 'Service']

function About() {
  const shouldReduceMotion = useReducedMotion()
  const reveal = { opacity: 0, y: shouldReduceMotion ? 0 : 18 }

  return (
    <div className="editorial-page">
      <Seo
        title="About"
        description="Learn about Alliance Yuwa Club, a youth-led organization in Biratnagar serving the community through leadership, civic awareness, culture, sport, and service since 2020."
        path="/about"
      />
      <section className="page-container about-hero" aria-labelledby="about-title">
        <motion.div initial={reveal} animate={{ opacity: 1, y: 0 }} transition={{ duration: shouldReduceMotion ? 0 : 0.45 }}>
          <p className="content-eyebrow">About Alliance Yuwa Club</p>
          <h1 id="about-title">A youth-led record of service in Biratnagar.</h1>
          <p>Alliance Yuwa Club brings young people together around community action, leadership, civic awareness, culture, sport, and service.</p>
        </motion.div>
        <MediaFrame
          className="about-hero__media"
          src={aboutImg}
          label="Alliance Yuwa Club community photograph"
          alt="Alliance Yuwa Club community activity"
        />      
      </section>

      <section className="about-story" aria-labelledby="story-title">
        <div className="page-container about-story__grid">
          <div>
            <p className="content-eyebrow">Our story</p>
            <h2 id="story-title">A shared beginning, a continuing commitment.</h2>
          </div>
          <div className="about-story__copy">
            <p>The club’s history includes its previous Shanti Yuwa Club identity and its continuing work today as Alliance Yuwa Club. Across that transition, the purpose has remained rooted in youth participation and community responsibility.</p>
            <p>For more than six years, members and volunteers have helped create a growing record of initiatives from Biratnagar and the surrounding community.</p>
          </div>
        </div>
      </section>

      <section className="page-container about-direction" aria-label="Alliance Yuwa Club mission, vision, and values">
        <article>
          <p className="content-eyebrow">Mission</p>
          <h2>Empower youth through meaningful action.</h2>
          <p>We organize opportunities for local youth to lead, serve, learn, and contribute to their community.</p>
        </article>
        <article>
          <p className="content-eyebrow">Vision</p>
          <h2>A connected community shaped by youth leadership.</h2>
          <p>We aim to strengthen public participation, collaboration, and positive action in Biratnagar.</p>
        </article>
      </section>

      <section className="about-history" aria-labelledby="history-title">
        <div className="page-container about-history__grid">
          <div>
            <p className="content-eyebrow">Six years of action</p>
            <h2 id="history-title">The work grows by showing up.</h2>
          </div>
          <ol>
            <li><span>2020</span><p>The club’s youth-led work took root in Biratnagar.</p></li>
            <li><span>2020–2025</span><p>Service, awareness, sports, cultural, and leadership initiatives built a sustained community record.</p></li>
            <li><span>Today</span><p>Alliance Yuwa Club continues that record with 100+ activities and a growing youth community.</p></li>
          </ol>
        </div>
      </section>

      <section className="page-container about-values" aria-labelledby="values-title">
        <p className="content-eyebrow">Core values</p>
        <h2 id="values-title">The principles behind the work.</h2>
        <ul>
          {values.map((value, index) => <li key={value}><span>0{index + 1}</span>{value}</li>)}
        </ul>
      </section>
    </div>
  )
}

export default About
