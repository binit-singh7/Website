import { useState } from 'react'

import { mediaUrl } from '../services/api'

function MediaFrame({ alt, className, label, src }) {
  const [failed, setFailed] = useState(false)

  if (src && !failed) {
    return <img className={className} src={mediaUrl(src)} alt={alt} loading="lazy" onError={() => setFailed(true)} />
  }

  return (
    <div className={`${className} media-frame`} aria-label={label} role="img">
      <svg className="media-frame__illustration" viewBox="0 0 160 120" aria-hidden="true">
        <path d="M18 91 55 54l25 22 23-31 39 46" fill="none" stroke="currentColor" strokeWidth="3" />
        <circle cx="111" cy="31" r="9" fill="currentColor" />
      </svg>
      <span>{label}</span>
    </div>
  )
}

export default MediaFrame
