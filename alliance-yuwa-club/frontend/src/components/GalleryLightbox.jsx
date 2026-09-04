import { AnimatePresence, motion, useReducedMotion } from 'framer-motion'
import { useEffect, useRef } from 'react'

import MediaFrame from './MediaFrame'
import './components.css'

function GalleryLightbox({ albumTitle, image, imageIndex, onClose, onNavigate, totalImages }) {
  const shouldReduceMotion = useReducedMotion()
  const dialogRef = useRef(null)
  const closeButtonRef = useRef(null)

  useEffect(() => {
    const previousFocus = document.activeElement
    const previousOverflow = document.body.style.overflow
    const dialog = dialogRef.current
    const focusableSelector = 'button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'

    closeButtonRef.current?.focus()
    document.body.style.overflow = 'hidden'

    function handleKeydown(event) {
      if (event.key === 'Escape') {
        event.preventDefault()
        onClose()
        return
      }

      if (event.key === 'ArrowLeft' && totalImages > 1) {
        event.preventDefault()
        onNavigate(-1)
        return
      }

      if (event.key === 'ArrowRight' && totalImages > 1) {
        event.preventDefault()
        onNavigate(1)
        return
      }

      if (event.key === 'Tab' && dialog) {
        const focusable = [...dialog.querySelectorAll(focusableSelector)]
        const first = focusable[0]
        const last = focusable.at(-1)
        if (!first || !last) return

        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault()
          last.focus()
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault()
          first.focus()
        }
      }
    }

    document.addEventListener('keydown', handleKeydown)
    return () => {
      document.removeEventListener('keydown', handleKeydown)
      document.body.style.overflow = previousOverflow
      previousFocus?.focus?.()
    }
  }, [onClose, onNavigate, totalImages])

  const caption = image.caption || `${albumTitle} photograph ${imageIndex + 1}`
  const motionProps = shouldReduceMotion
    ? { initial: false, animate: { opacity: 1 }, exit: { opacity: 0 }, transition: { duration: 0 } }
    : { initial: { opacity: 0 }, animate: { opacity: 1 }, exit: { opacity: 0 }, transition: { duration: 0.2 } }

  return (
    <AnimatePresence>
      <motion.div className="gallery-lightbox" {...motionProps} onMouseDown={(event) => event.target === event.currentTarget && onClose()}>
        <section ref={dialogRef} className="gallery-lightbox__dialog" role="dialog" aria-modal="true" aria-labelledby="gallery-lightbox-title" aria-describedby="gallery-lightbox-caption">
          <div className="gallery-lightbox__topbar">
            <p id="gallery-lightbox-title">{albumTitle} <span aria-hidden="true">·</span> {imageIndex + 1} of {totalImages}</p>
            <button ref={closeButtonRef} type="button" className="gallery-lightbox__button" onClick={onClose}><span aria-hidden="true">×</span><span className="sr-only">Close image viewer</span></button>
          </div>
          <div className="gallery-lightbox__content">
            {totalImages > 1 && <button type="button" className="gallery-lightbox__button gallery-lightbox__button--previous" onClick={() => onNavigate(-1)}><span aria-hidden="true">←</span><span className="sr-only">Previous photo</span></button>}
            <motion.div key={image.id} className="gallery-lightbox__media" initial={{ opacity: 0, scale: shouldReduceMotion ? 1 : 0.985 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: shouldReduceMotion ? 0 : 0.2 }}>
              <MediaFrame className="gallery-lightbox__image" src={image.image} alt={caption} label="Gallery photograph" />
            </motion.div>
            {totalImages > 1 && <button type="button" className="gallery-lightbox__button gallery-lightbox__button--next" onClick={() => onNavigate(1)}><span aria-hidden="true">→</span><span className="sr-only">Next photo</span></button>}
          </div>
          <p id="gallery-lightbox-caption" className="gallery-lightbox__caption">{caption}</p>
        </section>
      </motion.div>
    </AnimatePresence>
  )
}

export default GalleryLightbox
