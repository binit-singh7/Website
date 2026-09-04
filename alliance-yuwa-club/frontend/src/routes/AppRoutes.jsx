import { Route, Routes } from 'react-router-dom'

import App from '../App'
import LoadingState from '../components/LoadingState'
import NotFound from '../components/NotFound'
import FoundationPage from '../pages/FoundationPage'

const pageContent = {
  home: ['Alliance Yuwa Club', 'Unity. Leadership. Service.', 'The public website foundation is ready for the club’s verified stories, activities, and community information.'],
  about: ['About', 'Who we are.', 'Organization history and purpose will be added with verified club information.'],
  activities: ['Our Work', 'Programs in motion.', 'The activity archive foundation is ready for documented community work.'],
  activity: ['Our Work', 'Activity detail.', 'This activity’s complete report will appear here.'],
  events: ['Events', 'Gather, serve, lead.', 'Upcoming and past club events will be presented here.'],
  event: ['Events', 'Event detail.', 'Event information will be available here.'],
  news: ['News', 'From the club.', 'Official announcements and updates will appear here.'],
  article: ['News', 'News detail.', 'The full article will appear here.'],
  team: ['Team', 'People behind the work.', 'The executive committee and team will be introduced here.'],
  membership: ['Membership', 'Be part of the work.', 'Membership information and the application form will appear here.'],
  contact: ['Contact', 'Start a conversation.', 'Verified contact details and the contact form will appear here.'],
}

function page(key) {
  const [eyebrow, title, description] = pageContent[key]
  return <FoundationPage eyebrow={eyebrow} title={title} description={description} />
}

function AppRoutes() {
  return (
    <Routes>
      <Route element={<App />}>
        <Route index element={page('home')} />
        <Route path="about" element={page('about')} />
        <Route path="activities" element={page('activities')} />
        <Route path="activities/:slug" element={page('activity')} />
        <Route path="events" element={page('events')} />
        <Route path="events/:slug" element={page('event')} />
        <Route path="news" element={page('news')} />
        <Route path="news/:slug" element={page('article')} />
        <Route path="team" element={page('team')} />
        <Route path="membership" element={page('membership')} />
        <Route path="contact" element={page('contact')} />
        <Route path="loading" element={<LoadingState />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}

export default AppRoutes
