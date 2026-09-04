import { Link } from 'react-router-dom'

import PageContainer from './PageContainer'

function NotFound() {
  return (
    <PageContainer narrow>
      <section className="foundation-page">
        <p className="foundation-page__eyebrow">404</p>
        <h1 className="foundation-page__title">This page is not here.</h1>
        <p className="foundation-page__description">Return to the Alliance Yuwa Club homepage.</p>
        <p><Link to="/">Go home</Link></p>
      </section>
    </PageContainer>
  )
}

export default NotFound
