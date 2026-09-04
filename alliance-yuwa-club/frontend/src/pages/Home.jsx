import { motion, useReducedMotion } from 'framer-motion'
import { Link } from 'react-router-dom'

import borderCleanliness from '../assets/images/border-cleanliness.jpg'
import generalConvention from '../assets/images/general-convention.jpg'
import heroCommunity from '../assets/images/hero-community.jpg'
import womensSports from '../assets/images/womens-sports-festival.jpg'
import Button from '../components/Button'
import './Home.css'

const featuredActivities = [
  {
    category: 'Environment',
    date: '12 August 2026',
    location: 'Biratnagar–Jogbani (Rani) border area',
    title: 'International Youth Day Border Cleanliness Drive',
    summary: 'A community cleanup and plastics collection drive coordinated with local volunteers, Nepal Police, and metropolitan waste management.',
    to: '/activities/international-youth-day-border-cleanliness-awareness-drive',
    tone: 'green',
    image: borderCleanliness,
    imageAlt: 'Volunteers during the International Youth Day border cleanliness drive',
  },
  {
    category: 'Youth & Leadership',
    date: '15 August 2026',
    location: 'Biratnagar',
    title: 'First General Convention / Adhibheshana',
    summary: 'The club’s first general convention formalized leadership roles and the executive committee through an internal election.',
    to: '/events/first-general-convention-adhibheshana',
    tone: 'blue',
    image: generalConvention,
    imageAlt: 'Participants at the Alliance Yuwa Club general convention',
  },
  {
    category: 'Sports & Culture',
    date: 'June 2026',
    location: 'Biratnagar',
    title: "Women’s Sports and Cultural Festival 2083",
    summary: 'A community program bringing youth together through sports, participation, and cultural preservation.',
    to: '/activities/womens-sports-cultural-festival-2083',
    tone: 'orange',
    image: womensSports,
    imageAlt: 'Participants at the Women’s Sports and Cultural Festival 2083',
  },
]

const impactMetrics = [
  ['6+', 'Years of Leadership'],
  ['100+', 'Community Activities'],
  ['Biratnagar', '& Beyond'],
]

function Home() {
  const shouldReduceMotion = useReducedMotion()
  const reveal = {
    hidden: { opacity: 0, y: shouldReduceMotion ? 0 : 24 },
    visible: { opacity: 1, y: 0 },
  }
  const transition = { duration: shouldReduceMotion ? 0 : 0.55, ease: [0.22, 1, 0.36, 1] }
  const hover = shouldReduceMotion ? {} : { y: -5 }

  return (
    <div className="home-page">
      <section className="home-hero" aria-labelledby="home-hero-title">
        <div className="page-container home-hero__grid">
          <motion.div
            className="home-hero__content"
            initial="hidden"
            animate="visible"
            variants={reveal}
            transition={transition}
          >
            <p className="home-kicker">Alliance Yuwa Club · Biratnagar, Nepal</p>
            <h1 id="home-hero-title">Unity.<br />Leadership.<br /><em>Service.</em></h1>
            <p className="home-hero__intro">Youth-led action for a stronger, more connected community—organizing, serving, and creating change from Biratnagar.</p>
            <div className="home-actions">
              <Button to="/activities">Explore Activities</Button>
              <Button to="/membership" variant="secondary">Get Involved</Button>
            </div>
          </motion.div>
          <motion.aside
            className="home-hero__visual"
            initial="hidden"
            animate="visible"
            variants={reveal}
            transition={{ ...transition, delay: shouldReduceMotion ? 0 : 0.12 }}
          >
            <img className="home-hero__image" src={heroCommunity} alt="Alliance Yuwa Club youth volunteers in Biratnagar" />
          </motion.aside>
        </div>
      </section>

      <section className="home-impact" aria-label="Alliance Yuwa Club impact">
        <div className="page-container">
          <ul className="home-impact__list">
            {impactMetrics.map(([value, label], index) => (
              <motion.li
                key={value}
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true, amount: 0.45 }}
                variants={reveal}
                transition={{ ...transition, delay: shouldReduceMotion ? 0 : index * 0.08 }}
              >
                <strong>{value}</strong>
                <span>{label}</span>
              </motion.li>
            ))}
          </ul>
        </div>
      </section>

      <section className="home-featured page-container" aria-labelledby="featured-title">
        <motion.header
          className="home-section-heading"
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.4 }}
          variants={reveal}
          transition={transition}
        >
          <p className="home-kicker">Recent work</p>
          <h2 id="featured-title">The work leaves a record.</h2>
          <p>From public service to leadership and culture, each program is a step taken together.</p>
        </motion.header>
        <div className="home-featured__grid">
          {featuredActivities.map((activity, index) => (
            <motion.article
              key={activity.title}
              className={`activity-feature activity-feature--${activity.tone}`}
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, amount: 0.22 }}
              variants={reveal}
              transition={{ ...transition, delay: shouldReduceMotion ? 0 : index * 0.08 }}
              whileHover={hover}
            >
              <Link className="activity-feature__link" to={activity.to}>
                <div className="activity-feature__image">
                  <img src={activity.image} alt={activity.imageAlt} loading="lazy" />
                </div>
                <div className="activity-feature__body">
                  <p className="activity-feature__category">{activity.category}</p>
                  <p className="activity-feature__meta">{activity.date} <span aria-hidden="true">·</span> {activity.location}</p>
                  <h3>{activity.title}</h3>
                  <p>{activity.summary}</p>
                  <span className="activity-feature__cta">View activity <span aria-hidden="true">→</span></span>
                </div>
              </Link>
            </motion.article>
          ))}
        </div>
      </section>

      <section className="home-journey" aria-labelledby="journey-title">
        <div className="page-container home-journey__grid">
          <motion.header
            className="home-section-heading"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.35 }}
            variants={reveal}
            transition={transition}
          >
            <p className="home-kicker">Our journey</p>
            <h2 id="journey-title">Built through years of showing up.</h2>
            <p>Founded in 2020, the club has grown through consistent youth-led initiatives, community collaboration, and shared responsibility.</p>
            <Button to="/activities" variant="outline">Explore the activity archive</Button>
          </motion.header>
          <ol className="home-timeline">
            <li><span>2020</span><p>Alliance Yuwa Club began its youth-led journey in Biratnagar.</p></li>
            <li><span>2020–2025</span><p>Community service, awareness, sports, culture, and leadership activities built a record of action.</p></li>
            <li><span>Today</span><p>More than six years and 100+ activities continue to shape the club’s work and reach.</p></li>
          </ol>
        </div>
      </section>

      <motion.section
        className="home-community"
        aria-labelledby="community-title"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.28 }}
        variants={reveal}
        transition={transition}
      >
        <div className="page-container home-community__grid">
          <div>
            <p className="home-kicker">Community engagement</p>
            <h2 id="community-title">Be part of the work.</h2>
          </div>
          <div>
            <p>Join young people serving, organizing, and leading in our community—or start a conversation with the club.</p>
            <div className="home-actions">
              <Button to="/membership">Apply for membership</Button>
              <Button to="/contact" variant="secondary">Contact the club</Button>
            </div>
          </div>
        </div>
      </motion.section>
    </div>
  )
}

export default Home
