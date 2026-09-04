import { motion, useReducedMotion } from 'framer-motion'
import { Link, useParams } from 'react-router-dom'
import { useCallback, useEffect, useState } from 'react'

import GalleryLightbox from '../components/GalleryLightbox'
import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import { fetchGalleryAlbum } from '../services/api'
import { formatDate } from './contentUtils'
import { getAlbumTags } from './galleryUtils'
import './Gallery.css'

function GalleryDetail() {
  const { slug } = useParams()
  const shouldReduceMotion = useReducedMotion()
  const [album, setAlbum] = useState(null)
  const [notFound, setNotFound] = useState(false)
  const [error, setError] = useState(false)
  const [selectedPhoto, setSelectedPhoto] = useState(null)

  useEffect(() => {
    let isCurrent = true
    fetchGalleryAlbum(slug)
      .then((response) => {
        if (!isCurrent) return
        setAlbum(response)
        setNotFound(false)
        setError(false)
      })
      .catch((requestError) => {
        if (!isCurrent) return
        setAlbum(null)
        setNotFound(requestError.response?.status === 404)
        setError(requestError.response?.status !== 404)
      })

    return () => { isCurrent = false }
  }, [slug])

  const navigate = useCallback((direction) => {
    setSelectedPhoto((current) => ({ slug, index: (current.index + direction + album.images.length) % album.images.length }))
  }, [album, slug])

  const closeLightbox = useCallback(() => setSelectedPhoto(null), [])

  if (!album && !notFound && !error) return <LoadingState />

  if (notFound || error) {
    return <div className="page-container content-detail-message" role={error ? 'alert' : undefined}>
      <p className="content-eyebrow">Gallery</p>
      <h1>{notFound ? 'This album is not available.' : 'We could not load this album.'}</h1>
      <p>Return to the published photo archive to continue exploring the club’s work.</p>
      <Link className="text-link" to="/gallery">Back to gallery</Link>
    </div>
  }

  const tags = getAlbumTags(album)
  const selectedIndex = selectedPhoto?.slug === slug ? selectedPhoto.index : null
  const selectedImage = selectedIndex === null ? null : album.images[selectedIndex]

  return (
    <article className="gallery-detail">
      <motion.header className="page-container gallery-detail__hero" initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 18 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: shouldReduceMotion ? 0 : 0.4 }}>
        <Link className="text-link" to="/gallery">← Back to gallery</Link>
        <p className="content-eyebrow">Photo album</p>
        <h1>{album.title}</h1>
        <div className="gallery-detail__metadata">
          <time dateTime={album.date}>{formatDate(album.date)}</time>
          {tags.map((tag) => <span key={tag}>{tag}</span>)}
        </div>
        {album.description && <p>{album.description}</p>}
      </motion.header>

      <section className="page-container gallery-detail__photos" aria-labelledby="album-photos-title">
        <div className="gallery-detail__heading">
          <div><p className="content-eyebrow">{album.images.length} {album.images.length === 1 ? 'photograph' : 'photographs'}</p><h2 id="album-photos-title">Browse the album</h2></div>
          <p>Select a photo to view it in full screen. Use the arrow keys to move between images and Escape to close.</p>
        </div>
        {album.images.length ? <div className="album-photos">
          {album.images.map((image, index) => {
            const label = image.caption || `${album.title} photograph ${index + 1}`
            return <motion.figure key={image.id} className="gallery-photo" initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: shouldReduceMotion ? 0 : 0.3, delay: shouldReduceMotion ? 0 : Math.min(index * 0.03, 0.18) }}>
              <button type="button" onClick={() => setSelectedPhoto({ slug, index })} aria-label={`View ${label} in full screen`}>
                <MediaFrame className="gallery-photo__image" src={image.image} alt={label} label="Gallery photograph" />
              </button>
              {image.caption && <figcaption>{image.caption}</figcaption>}
            </motion.figure>
          })}
        </div> : <div className="content-message">Photographs for this published album will appear here when they are added.</div>}
      </section>

      {selectedImage && <GalleryLightbox albumTitle={album.title} image={selectedImage} imageIndex={selectedIndex} totalImages={album.images.length} onClose={closeLightbox} onNavigate={navigate} />}
    </article>
  )
}

export default GalleryDetail
