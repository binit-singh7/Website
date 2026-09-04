import { motion, useReducedMotion } from 'framer-motion'
import { useEffect, useState } from 'react'

import Button from '../components/Button'
import Seo from '../components/Seo'
import { fetchOrganization, submitContactMessage } from '../services/api'
import { getSubmissionErrors, getSubmissionMessage, isValidEmail, required } from './formUtils'
import './FormPages.css'

const initialForm = { name: '', email: '', subject: '', message: '' }

function validate(form) {
  const errors = {
    name: required(form.name, 'Enter your name.'),
    email: required(form.email, 'Enter your email address.'),
    subject: required(form.subject, 'Enter a subject.'),
    message: required(form.message, 'Enter your message.'),
  }
  if (form.email && !isValidEmail(form.email)) errors.email = 'Enter a valid email address.'
  return Object.fromEntries(Object.entries(errors).filter(([, message]) => message))
}

function Contact() {
  const shouldReduceMotion = useReducedMotion()
  const [organization, setOrganization] = useState(null)
  const [form, setForm] = useState(initialForm)
  const [errors, setErrors] = useState({})
  const [submitError, setSubmitError] = useState('')
  const [successMessage, setSuccessMessage] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  useEffect(() => {
    let isCurrent = true
    fetchOrganization().then((data) => isCurrent && setOrganization(data)).catch(() => isCurrent && setOrganization({}))
    return () => { isCurrent = false }
  }, [])

  const reveal = {
    hidden: { opacity: 0, y: shouldReduceMotion ? 0 : 18 },
    visible: { opacity: 1, y: 0 },
  }
  const transition = { duration: shouldReduceMotion ? 0 : 0.4, ease: [0.22, 1, 0.36, 1] }

  function updateField(event) {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
    setErrors((current) => ({ ...current, [name]: '' }))
    setSubmitError('')
  }

  async function handleSubmit(event) {
    event.preventDefault()
    const nextErrors = validate(form)
    setErrors(nextErrors)
    setSubmitError('')
    if (Object.keys(nextErrors).length) return

    setIsSubmitting(true)
    try {
      const response = await submitContactMessage({
        ...form,
        name: form.name.trim(),
        email: form.email.trim(),
        subject: form.subject.trim(),
        message: form.message.trim(),
      })
      setSuccessMessage(response.message || 'Your message has been submitted successfully.')
      setForm(initialForm)
    } catch (error) {
      setErrors(getSubmissionErrors(error))
      setSubmitError(getSubmissionMessage(error, 'We could not send your message. Please review the form and try again.'))
    } finally {
      setIsSubmitting(false)
    }
  }

  const socialLinks = [
    ['Facebook', organization?.facebook_url],
    ['Instagram', organization?.instagram_url],
    ['YouTube', organization?.youtube_url],
  ].filter(([, url]) => url)

  return (
    <div className="form-page">
      <Seo
        title="Contact"
        description="Contact Alliance Yuwa Club in Biratnagar for questions, ideas, partnerships, or to get involved with our community work."
        path="/contact"
      />
      <section className="form-page__hero form-page__hero--contact">
        <div className="page-container">
          <motion.header className="form-page__hero-copy" initial="hidden" animate="visible" variants={reveal} transition={transition}>
            <p className="content-eyebrow">Contact</p>
            <h1>Start a conversation.</h1>
            <p>Questions, ideas, partnerships, or a wish to get involved—send a message to Alliance Yuwa Club in Biratnagar.</p>
          </motion.header>
        </div>
      </section>

      <section className="page-container contact-layout" aria-labelledby="contact-form-title">
        <motion.aside className="contact-details" initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.2 }} variants={reveal} transition={transition}>
          <p className="content-eyebrow">Find the club</p>
          <h2>Alliance Yuwa Club</h2>
          <dl>
            <div><dt>Location</dt><dd>{organization?.address || 'Biratnagar, Nepal'}</dd></div>
            <div><dt>Email</dt><dd>{organization?.email ? <a href={`mailto:${organization.email}`}>{organization.email}</a> : 'Official email will be published here.'}</dd></div>
            <div><dt>Phone</dt><dd>{organization?.phone ? <a href={`tel:${organization.phone.replace(/\s/g, '')}`}>{organization.phone}</a> : 'Official phone number will be published here.'}</dd></div>
          </dl>
          <div className="contact-details__social">
            <h3>Follow the club</h3>
            {socialLinks.length ? <ul>{socialLinks.map(([name, url]) => <li key={name}><a href={url} target="_blank" rel="noreferrer">{name}<span className="sr-only"> (opens in a new tab)</span></a></li>)}</ul> : <p>Official social links will be published once verified.</p>}
          </div>
        </motion.aside>

        <motion.div className="contact-form-wrap" initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.2 }} variants={reveal} transition={{ ...transition, delay: shouldReduceMotion ? 0 : 0.08 }}>
          <p className="content-eyebrow">Send an inquiry</p>
          <h2 id="contact-form-title">How can we help?</h2>
          <p>We will use the details below only to respond to your message.</p>
          {successMessage && <div className="form-notice form-notice--success" role="status" aria-live="polite">{successMessage}</div>}
          <form className="club-form" noValidate onSubmit={handleSubmit}>
            {submitError && <div className="form-notice form-notice--error" role="alert">{submitError}</div>}
            <ContactField label="Name" name="name" value={form.name} error={errors.name} onChange={updateField} autoComplete="name" />
            <ContactField label="Email address" name="email" type="email" value={form.email} error={errors.email} onChange={updateField} autoComplete="email" />
            <ContactField label="Subject" name="subject" value={form.subject} error={errors.subject} onChange={updateField} />
            <div className="form-field">
              <label htmlFor="contact-message">Message</label>
              <textarea id="contact-message" name="message" value={form.message} onChange={updateField} aria-invalid={Boolean(errors.message)} aria-describedby={errors.message ? 'contact-message-error' : undefined} required rows="7" />
              {errors.message && <p id="contact-message-error" className="field-error">{errors.message}</p>}
            </div>
            <div className="club-form__actions"><Button type="submit" disabled={isSubmitting}>{isSubmitting ? 'Sending message…' : 'Send message'}</Button></div>
          </form>
        </motion.div>
      </section>
    </div>
  )
}

function ContactField({ label, name, type = 'text', value, error, ...props }) {
  const id = `contact-${name}`
  return (
    <div className="form-field">
      <label htmlFor={id}>{label}</label>
      <input id={id} name={name} type={type} value={value} onChange={props.onChange} aria-invalid={Boolean(error)} aria-describedby={error ? `${id}-error` : undefined} required {...props} />
      {error && <p id={`${id}-error`} className="field-error">{error}</p>}
    </div>
  )
}

export default Contact
