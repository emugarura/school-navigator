from django.forms import ModelForm
import schools.models as schools_models

class SchoolProfileForm(ModelForm):
    class Meta:
        model = schools_models.SchoolProfile
        exclude = ('school', 'created_at', 'submitted_at', )

    _fieldsets = (
        ('Basic Facts', [
            'level', 'grade_min', 'grade_max', 'phone_number',
            'website_url', 'year_opened', 'mission_statement',
            'theme', 'uniform_required',
        ]),
        ('Points of Pride', [
            'points_of_pride1', 'points_of_pride2', 'points_of_pride3',
        ]),
        ('School Services', [
            'transportation', 'transportation_explanation',
            'extended_care_offered', 'before_care_hours',
            'after_care_hours', 'extended_care_cost',
            'extended_care_financial_assistance',
            'breakfast_served', 'breakfast_free_and_reduced',
            'breakfast_explanation', 
            'lunch_served', 'lunch_free_and_reduced',
            'lunch_explanation',
        ]),
        ('School Leadership', [
            'principal_name', 'principal_start_year', 'principal_bio',
        ]),
        ('Admissions Policy', [
            'admissions_policy_type',
            'lottery_priority_1', 'lottery_priority_2', 'lottery_priority_3',
            'lottery_priority_4', 'lottery_priority_5',
            'lottery_deadline', 'learn_more_link',
        ]),
        ('Targeted Academic Offerings', [
            'english_language_learner',
            'special_education',
            'gifted_education',
            'other_academic',
        ]),
        ('Extracurricular Offerings', [
            'academic', 'arts', 'sports', 'service_leadership', 'other',
        ]),
        ('Parent Involvement', [
            'pta', 'pta_website', 'parental_involvement_notes',
        ]),
        ('Your Feedback', [
            'survey_feedback',
        ]),

    )

    @property
    def fieldsets(self):
        for description, fields in self._fieldsets:
            yield description, [self[field] for field in fields]

    # basic_facts

    # school_services

    # school_leadership

    # admissions_policy

    # targeted_admissions_policy

    # extracurricular_offerings

    # parent_involvement

    # feedback
