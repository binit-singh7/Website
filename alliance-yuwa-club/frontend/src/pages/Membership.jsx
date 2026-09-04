import { motion, useReducedMotion } from 'framer-motion'
import { useState } from 'react'

import Button from '../components/Button'
import Seo from '../components/Seo'
import { submitMembershipApplication } from '../services/api'
import {
  getSubmissionErrors,
  getSubmissionMessage,
  isValidEmail,
  isValidPhone,
  required,
} from './formUtils'
import './FormPages.css'

const interestOptions = [
  'Community service',
  'Environment',
  'Youth leadership',
  'Sports',
  'Culture and arts',
  'Public awareness',
]

const initialForm = {
  full_name: '',
  email: '',
  phone: '',
  date_of_birth: '',
  address: '',
  ward: '',
  occupation: '',
  education: '',
  areas_of_interest: [],
  reason_for_joining: '',
}

function validate(form) {
  const errors = {
    full_name: required(form.full_name, 'Enter your full name.'),
    email: required(form.email, 'Enter your email address.'),
    phone: required(form.phone, 'Enter your phone number.'),
    date_of_birth: required(form.date_of_birth, 'Select your date of birth.'),
    address: required(form.address, 'Enter your address.'),
    ward: required(form.ward, 'Enter your ward number or name.'),
    occupation: required(form.occupation, 'Enter your occupation.'),
    education: required(form.education, 'Enter your education level.'),
    areas_of_interest: form.areas_of_interest.length ? '' : 'Choose at least one area of interest.',
    reason_for_joining: required(form.reason_for_joining, 'Tell us why you would like to join.'),
  }

  if (form.email && !isValidEmail(form.email)) errors.email = 'Enter a valid email address.'
  if (form.phone && !isValidPhone(form.phone)) errors.phone = 'Enter a valid phone number.'
  if (form.date_of_birth && form.date_of_birth > new Date().toISOString().slice(0, 10)) {
    errors.date_of_birth = 'Date of birth cannot be in the future.'
  }

  return Object.fromEntries(Object.entries(errors).filter(([, message]) => message))
}

function Membership() {
  const shouldReduceMotion = useReducedMotion()
  const [form, setForm] = useState(initialForm)
  const [errors, setErrors] = useState({})
  const [submitError, setSubmitError] = useState('')
  const [successMessage, setSuccessMessage] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

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

  function toggleInterest(event) {
    const { checked, value } = event.target
    setForm((current) => ({
      ...current,
      areas_of_interest: checked
        ? [...current.areas_of_interest, value]
        : current.areas_of_interest.filter((interest) => interest !== value),
    }))
    setErrors((current) => ({ ...current, areas_of_interest: '' }))
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
      const response = await submitMembershipApplication({
        ...form,
        full_name: form.full_name.trim(),
        email: form.email.trim(),
        phone: form.phone.trim(),
        address: form.address.trim(),
        ward: form.ward.trim(),
        occupation: form.occupation.trim(),
        education: form.education.trim(),
        reason_for_joining: form.reason_for_joining.trim(),
      })
      setSuccessMessage(response.message || 'Membership application submitted successfully.')
    } catch (error) {
      const responseErrors = getSubmissionErrors(error)
      setErrors(responseErrors)
      setSubmitError(getSubmissionMessage(error, 'We could not submit your application. Please review the form and try again.'))
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="form-page">
      <Seo
        title="Membership"
        description="Apply to join Alliance Yuwa Club and take part in community service, environmental action, culture, sports, and youth leadership in Biratnagar."
        path="/membership"
      />
      <section className="form-page__hero">
        <div className="page-container form-page__hero-grid">
          <motion.header initial="hidden" animate="visible" variants={reveal} transition={transition}>
            <p className="content-eyebrow">Membership</p>
            <h1>Bring your energy to work that matters.</h1>
            <p>Alliance Yuwa Club brings young people in Biratnagar together to serve, organize, learn, and lead with purpose.</p>
          </motion.header>
          <motion.aside className="membership-invitation" initial="hidden" animate="visible" variants={reveal} transition={{ ...transition, delay: shouldReduceMotion ? 0 : 0.1 }}>
            <p className="content-eyebrow">What membership means</p>
            <ul>
              <li>Take part in community service, environmental action, culture, sports, and public-awareness work.</li>
              <li>Build practical leadership through shared responsibility and local collaboration.</li>
              <li>Join with a willingness to contribute respectfully, consistently, and as part of a team.</li>
            </ul>
            <p className="membership-invitation__note">Applications are reviewed by the club. Submitting this form does not create membership automatically.</p>
          </motion.aside>
        </div>
      </section>

      <section className="page-container form-page__content" aria-labelledby="membership-form-title">
        <motion.div initial="hidden" whileInView="visible" viewport={{ once: true, amount: 0.2 }} variants={reveal} transition={transition}>
          <p className="content-eyebrow">Application</p>
          <h2 id="membership-form-title">Tell us about yourself.</h2>
          <p>All fields help the club review your application. We will use this information only for membership processing.</p>
        </motion.div>

        {successMessage ? (
          <div className="form-notice form-notice--success" role="status" aria-live="polite">
            <h2>Thank you for applying.</h2>
            <p>{successMessage} The club will review your application and follow up using the contact details you provided.</p>
            <Button type="button" variant="outline" onClick={() => { setForm(initialForm); setSuccessMessage(''); setErrors({}) }}>Submit another application</Button>
          </div>
        ) : (
          <form className="club-form" noValidate onSubmit={handleSubmit}>
            {submitError && <div className="form-notice form-notice--error" role="alert">{submitError}</div>}
            <div className="club-form__grid">
              <Field label="Full name" name="full_name" value={form.full_name} error={errors.full_name} onChange={updateField} autoComplete="name" />
              <Field label="Email address" name="email" type="email" value={form.email} error={errors.email} onChange={updateField} autoComplete="email" />
              <Field label="Phone number" name="phone" type="tel" value={form.phone} error={errors.phone} onChange={updateField} autoComplete="tel" />
              <Field label="Date of birth" name="date_of_birth" type="date" value={form.date_of_birth} error={errors.date_of_birth} onChange={updateField} max={new Date().toISOString().slice(0, 10)} />
              <Field label="Address" name="address" value={form.address} error={errors.address} onChange={updateField} autoComplete="street-address" />
              <Field label="Ward" name="ward" value={form.ward} error={errors.ward} onChange={updateField} hint="For example, Ward 10." />
              <Field label="Occupation" name="occupation" value={form.occupation} error={errors.occupation} onChange={updateField} />
              <Field label="Education" name="education" value={form.education} error={errors.education} onChange={updateField} hint="Your current or highest level of education." />
            </div>

            <fieldset className="club-form__fieldset" aria-describedby={errors.areas_of_interest ? 'membership-areas_of_interest-error' : 'membership-interests-help'}>
              <legend>Skills and interests</legend>
              <p id="membership-interests-help">Choose the areas where you would most like to participate.</p>
              <div className="club-form__choices">
                {interestOptions.map((interest) => (
                  <label key={interest} className="choice-control">
                    <input type="checkbox" value={interest} checked={form.areas_of_interest.includes(interest)} onChange={toggleInterest} aria-invalid={Boolean(errors.areas_of_interest)} />
                    <span>{interest}</span>
                  </label>
                ))}
              </div>
              {errors.areas_of_interest && <p id="membership-areas_of_interest-error" className="field-error">{errors.areas_of_interest}</p>}
            </fieldset>

            <div className="form-field">
              <label htmlFor="membership-reason_for_joining">Why would you like to join?</label>
              <textarea id="membership-reason_for_joining" name="reason_for_joining" value={form.reason_for_joining} onChange={updateField} aria-invalid={Boolean(errors.reason_for_joining)} aria-describedby={errors.reason_for_joining ? 'membership-reason_for_joining-error' : undefined} rows="6" />
              {errors.reason_for_joining && <p id="membership-reason_for_joining-error" className="field-error">{errors.reason_for_joining}</p>}
            </div>
            <div className="club-form__actions">
              <Button type="submit" disabled={isSubmitting}>{isSubmitting ? 'Submitting application…' : 'Submit application'}</Button>
              <p>We will contact you after the application has been reviewed.</p>
            </div>
          </form>
        )}
      </section>
    </div>
  )
}

function Field({ label, name, type = 'text', value, error, hint, ...props }) {
  const id = `membership-${name}`
  const describedBy = [hint ? `${id}-hint` : '', error ? `${id}-error` : ''].filter(Boolean).join(' ') || undefined

  return (
    <div className="form-field">
      <label htmlFor={id}>{label}</label>
      <input id={id} name={name} type={type} value={value} aria-invalid={Boolean(error)} aria-describedby={describedBy} required {...props} />
      {hint && <p id={`${id}-hint`} className="field-hint">{hint}</p>}
      {error && <p id={`${id}-error`} className="field-error">{error}</p>}
    </div>
  )
}

export default Membership
