import { motion, useReducedMotion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { useEffect, useMemo, useState } from 'react'

import LoadingState from '../components/LoadingState'
import MediaFrame from '../components/MediaFrame'
import { fetchGalleryAlbum, fetchGalleryAlbums } from '../services/api'
import { collectionResult, formatDate } from './contentUtils'
import { getAlbumTags, getPhotoCount } from './galleryUtils'
import './Gallery.css'

function Gallery() {
  const shouldReduceMotion = useReducedMotion()
  const [page, setPage] = useState(1)
  const [albums, setAlbums] = useState(null)
  const [error, setError] = useState(false)
  const [activeTag, setActiveTag] = useState('All')

  useEffect(() => {
    let isCurrent = true

    async function loadAlbums() {
      try {
        const response = collectionResult(await fetchGalleryAlbums({ page, pageSize: 12 }))
        const enrichedAlbums = await Promise.all(response.results.map(async (album) => {
          try {
            const detail = await fetchGalleryAlbum(album.slug)
            return { ...album, photoCount: getPhotoCount(detail), tags: getAlbumTags(detail) }
          } catch {
            return { ...album, photoCount: getPhotoCount(album), tags: getAlbumTags(album) }
          }
        }))

        if (!isCurrent) return
        setAlbums({ ...response, results: enrichedAlbums })
        setError(false)
      } catch {
        if (isCurrent) setError(true)
      }
    }

    loadAlbums()
    return () => { isCurrent = false }
  }, [page])

  const tags = useMemo(() => ['All', ...new Set(albums?.results.flatMap(getAlbumTags) || [])], [albums])
  const visibleAlbums = albums?.results.filter((album) => activeTag === 'All' || getAlbumTags(album).includes(activeTag)) || []

  function selectTag(tag) {
    setActiveTag(tag)
  }

  if (!albums && !error) return <LoadingState />

  return (
    <div className="gallery-page">
      <header className="page-container gallery-intro">
        <p className="content-eyebrow">Gallery</p>
        <h1>The moments behind the work.</h1>
        <p>Browse published photographs from Alliance Yuwa Club activities, gatherings, and community action in Biratnagar.</p>
      </header>

      <section className="page-container gallery-archive" aria-labelledby="gallery-albums-title">
        <div className="gallery-archive__heading">
          <div>
            <p className="content-eyebrow">Photo archive</p>
            <h2 id="gallery-albums-title">Published albums</h2>
          </div>
          {tags.length > 1 && <div className="filter-group gallery-filter">
            <p id="gallery-filter-label">Filter by tag</p>
            <div className="filter-bar" role="toolbar" aria-labelledby="gallery-filter-label">
              {tags.map((tag) => <button key={tag} type="button" className={activeTag === tag ? 'filter-button filter-button--active' : 'filter-button'} aria-pressed={activeTag === tag} onClick={() => selectTag(tag)}>{tag}</button>)}
            </div>
          </div>}
        </div>

        {error ? (
          <div className="content-message" role="alert">Unable to load the photo archive right now. Please try again shortly.</div>
        ) : visibleAlbums.length === 0 ? (
          <div className="content-message">No published albums match this filter yet.</div>
        ) : (
          <div className="album-grid">
            {visibleAlbums.map((album, index) => (
              <motion.article key={album.id} className="album-card" initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 16 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: shouldReduceMotion ? 0 : 0.35, delay: shouldReduceMotion ? 0 : index * 0.04 }} whileHover={shouldReduceMotion ? {} : { y: -4 }}>
                <Link to={`/gallery/${album.slug}`}>
                  <div className="album-card__media">
                    <MediaFrame className="album-card__image" src={album.cover_image} alt={`${album.title} album cover`} label="Gallery album cover" />
                    <span className="album-card__count">{album.photoCount === null ? 'Photo album' : `${album.photoCount} ${album.photoCount === 1 ? 'photo' : 'photos'}`}</span>
                  </div>
                  <div className="album-card__body">
                    <p className="album-card__date"><time dateTime={album.date}>{formatDate(album.date)}</time></p>
                    <h3>{album.title}</h3>
                    {getAlbumTags(album).length > 0 && <ul className="album-card__tags" aria-label="Album tags">{getAlbumTags(album).map((tag) => <li key={tag}>{tag}</li>)}</ul>}
                    <span className="record-card__link">Open album <span aria-hidden="true">→</span></span>
                  </div>
                </Link>
              </motion.article>
            ))}
          </div>
        )}
        {albums && albums.count > albums.results.length && (
          <nav className="content-pagination" aria-label="Gallery pages">
            <button type="button" disabled={!albums.previous} onClick={() => setPage((current) => current - 1)}>Previous</button>
            <span>Page {page}</span>
            <button type="button" disabled={!albums.next} onClick={() => setPage((current) => current + 1)}>Next</button>
          </nav>
        )}
      </section>
    </div>
  )
}

export default Gallery
