import { Route, Routes } from 'react-router-dom'

import App from '../App'
import LoadingState from '../components/LoadingState'
import NotFound from '../components/NotFound'
import Activities from '../pages/Activities'
import ActivityDetail from '../pages/ActivityDetail'
import About from '../pages/About'
import EventDetail from '../pages/EventDetail'
import Events from '../pages/Events'
import FoundationPage from '../pages/FoundationPage'
import Home from '../pages/Home'
import News from '../pages/News'
import NewsDetail from '../pages/NewsDetail'
import Team from '../pages/Team'

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
        <Route index element={<Home />} />
        <Route path="about" element={<About />} />
        <Route path="activities" element={<Activities />} />
        <Route path="activities/:slug" element={<ActivityDetail />} />
        <Route path="events" element={<Events />} />
        <Route path="events/:slug" element={<EventDetail />} />
        <Route path="news" element={<News />} />
        <Route path="news/:slug" element={<NewsDetail />} />
        <Route path="team" element={<Team />} />
        <Route path="membership" element={page('membership')} />
        <Route path="contact" element={page('contact')} />
        <Route path="loading" element={<LoadingState />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}

export default AppRoutes
