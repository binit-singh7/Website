import { Link } from 'react-router-dom'

import './components.css'

function Footer() {
  return (
    <footer className="footer">
      <div className="page-container footer__grid">
        <div>
          <p className="footer__name">Alliance Yuwa Club</p>
          <p className="footer__motto">Unity, Leadership, and Service.</p>
        </div>
        <nav aria-label="Footer navigation">
          <Link to="/activities">Our Work</Link>
          <Link to="/events">Events</Link>
          <Link to="/contact">Contact</Link>
        </nav>
        <div className="footer__contact">
          <p>Biratnagar, Nepal</p>
          <Link to="/contact">Contact the club</Link>
        </div>
        <div className="footer__social" aria-label="Social links">
          <p>Official social links will be added from verified organization data.</p>
        </div>
      </div>
      <div className="page-container footer__bottom">© {new Date().getFullYear()} Alliance Yuwa Club</div>
    </footer>
  )
}

export default Footer
