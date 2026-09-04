import { Link } from 'react-router-dom'

import './components.css'

function Button({ children, to, variant = 'primary', type = 'button', ...props }) {
  const className = `button button--${variant}`

  if (to) {
    return <Link className={className} to={to}>{children}</Link>
  }

  return <button className={className} type={type} {...props}>{children}</button>
}

export default Button
