import PageContainer from './PageContainer'

function LoadingState() {
  return (
    <PageContainer narrow>
      <section className="loading-state" aria-live="polite">
        <p>Loading Alliance Yuwa Club…</p>
      </section>
    </PageContainer>
  )
}

export default LoadingState
