import PageContainer from '../components/PageContainer'

function FoundationPage({ eyebrow, title, description }) {
  return (
    <PageContainer>
      <section className="foundation-page">
        <p className="foundation-page__eyebrow">{eyebrow}</p>
        <h1 className="foundation-page__title">{title}</h1>
        <p className="foundation-page__description">{description}</p>
      </section>
    </PageContainer>
  )
}

export default FoundationPage
