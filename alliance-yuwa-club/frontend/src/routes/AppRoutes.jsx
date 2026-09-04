import { Route, Routes } from 'react-router-dom'

import App from '../App'
import LoadingState from '../components/LoadingState'
import NotFound from '../components/NotFound'
import Activities from '../pages/Activities'
import ActivityDetail from '../pages/ActivityDetail'
import About from '../pages/About'
import Contact from '../pages/Contact'
import EventDetail from '../pages/EventDetail'
import Events from '../pages/Events'
import Home from '../pages/Home'
import Membership from '../pages/Membership'
import News from '../pages/News'
import NewsDetail from '../pages/NewsDetail'
import Team from '../pages/Team'

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
        <Route path="membership" element={<Membership />} />
        <Route path="contact" element={<Contact />} />
        <Route path="loading" element={<LoadingState />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}

export default AppRoutes
