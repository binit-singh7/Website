export function getAlbumTags(album) {
  const tags = album.tags || album.categories || album.category || []
  const values = Array.isArray(tags) ? tags : [tags]

  return values
    .map((tag) => (typeof tag === 'string' ? tag : tag?.name))
    .filter(Boolean)
}

export function getPhotoCount(album) {
  if (typeof album.photo_count === 'number') return album.photo_count
  if (typeof album.image_count === 'number') return album.image_count
  if (Array.isArray(album.images)) return album.images.length
  return null
}
