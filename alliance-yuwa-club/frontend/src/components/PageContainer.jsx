function PageContainer({ children, narrow = false, className = '' }) {
  const classes = ['page-container', narrow && 'page-container--narrow', className]
    .filter(Boolean)
    .join(' ')

  return <div className={classes}>{children}</div>
}

export default PageContainer
