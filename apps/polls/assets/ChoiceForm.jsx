const React = require('react')
const django = require('django')
const ErrorList = require('../../contrib/assets/ErrorList')

const ChoiceForm = (props) => {
  return (
    <div className="form-group form-group--narrow form-inline">
      <div>
        <label htmlFor={'id_choices-' + props.id + '-name'} className="input-group">
          <span className="visually-hidden">{props.label}</span>
          <input
            id={'id_choices-' + props.id + '-name'}
            name={'choices-' + props.id + '-name'}
            type="text"
            className="form-control"
            value={props.choice.label}
            onChange={(e) => { props.onLabelChange(e.target.value) }}
          />
        </label>
        <button
          className="btn btn--light btn--append"
          onClick={props.onDelete}
          title={django.gettext('remove')}
          type="button"
        >
          <i
            className="fa fa-times"
            aria-label={django.gettext('remove')}
          />
        </button>
      </div>
      <ErrorList errors={props.errors} field="label" />
    </div>
  )
}

module.exports = ChoiceForm
