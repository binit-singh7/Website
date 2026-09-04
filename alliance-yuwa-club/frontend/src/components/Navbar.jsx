import { useState } from 'react'
import { NavLink } from 'react-router-dom'

import logo from '../assets/logo.svg'
import Button from './Button'
import './components.css'

const navigation = [
  { label: 'About', to: '/about' },
  { label: 'Our Work', to: '/activities' },
  { label: 'Events', to: '/events' },
  { label: 'News', to: '/news' },
  { label: 'Team', to: '/team' },
]

function Navbar() {
  const [isOpen, setIsOpen] = useState(false)
  const closeMenu = () => setIsOpen(false)

  return (
    <header className="navbar">
      <div className="page-container navbar__inner">
        <NavLink className="wordmark" to="/" onClick={closeMenu} aria-label="Alliance Yuwa Club home">
          <img className="wordmark__logo" src={logo} alt="Alliance Yuwa Club Logo" />
        </NavLink>
        <button
          className="navbar__toggle"
          type="button"
          aria-expanded={isOpen}
          aria-controls="primary-navigation"
          onClick={() => setIsOpen((open) => !open)}
        >
          <span className="sr-only">{isOpen ? 'Close' : 'Open'} navigation</span>
          <span aria-hidden="true">{isOpen ? '×' : 'Menu'}</span>
        </button>
        <nav id="primary-navigation" className={`navbar__nav ${isOpen ? 'navbar__nav--open' : ''}`} aria-label="Primary navigation">
          {navigation.map(({ label, to }) => (
            <NavLink key={to} className="navbar__link" to={to} onClick={closeMenu}>
              {label}
            </NavLink>
          ))}
          <Button to="/membership" variant="outline">Join us</Button>
        </nav>
      </div>
    </header>
  )
}

export default Navbar
