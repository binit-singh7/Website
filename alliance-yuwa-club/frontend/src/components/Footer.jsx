import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

import logo from '../assets/logo.svg'
import { fetchOrganization } from '../services/api'
import './components.css'

function Footer() {
  const [organization, setOrganization] = useState(null)

  useEffect(() => {
    let isCurrent = true

    fetchOrganization()
      .then((data) => isCurrent && setOrganization(data))
      .catch(() => isCurrent && setOrganization({}))

    return () => { isCurrent = false }
  }, [])

  const socialLinks = [
    ['Facebook', organization?.facebook_url],
    ['Instagram', organization?.instagram_url],
    ['YouTube', organization?.youtube_url],
    ['TikTok', organization?.tiktok_url],
  ].filter(([, url]) => url)

  return (
    <footer className="footer">
      <div className="page-container footer__grid">
        <div>
          <img className="footer__logo" src={logo} alt="Alliance Yuwa Club Logo" />
          <p className="footer__motto">Unity, Leadership, and Service.</p>
        </div>
        <nav aria-label="Footer navigation">
          <Link to="/activities">Our Work</Link>
          <Link to="/events">Events</Link>
          <Link to="/gallery">Gallery</Link>
          <Link to="/contact">Contact</Link>
        </nav>
        <div className="footer__contact">
          <p>Biratnagar, Nepal</p>
          <Link to="/contact">Contact the club</Link>
        </div>
        {socialLinks.length > 0 && (
          <div className="footer__social">
            <p>Follow us</p>
            <nav aria-label="Social links">
              {socialLinks.map(([name, url]) => (
                <a key={name} href={url} target="_blank" rel="noreferrer">
                  {name}<span className="sr-only"> (opens in a new tab)</span>
                </a>
              ))}
            </nav>
          </div>
        )}
      </div>
      <div className="page-container footer__bottom">© {new Date().getFullYear()} Alliance Yuwa Club</div>
    </footer>
  )
}

export default Footer
