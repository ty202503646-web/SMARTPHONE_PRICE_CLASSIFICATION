from django import forms

class SmartphoneForm(forms.Form):

    ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": field.label
            })
    battery_power = forms.FloatField(
        label="Battery Capacity",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Enter battery capacity in mAh (e.g. 2000)"
        })
    )

    blue = forms.ChoiceField(
        label="Bluetooth",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={"class": "form-select"})
    )

    clock_speed = forms.FloatField(
        label="Processor Speed",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Enter GHz (e.g. 2.0)"
        })
    )

    dual_sim = forms.ChoiceField(
        label="Dual SIM",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={"class": "form-select"})
    )

    fc = forms.FloatField(
        label="Front Camera (MP)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 5"
        })
    )

    four_g = forms.ChoiceField(
        label="4G Support",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={"class": "form-select"})
    )

    int_memory = forms.FloatField(
        label="Internal Storage (GB)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 64"
        })
    )

    m_dep = forms.FloatField(
        label="Thickness",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 0.5 cm"
        })
    )

    mobile_wt = forms.FloatField(
        label="Weight (g)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 150"
        })
    )

    n_cores = forms.FloatField(
        label="CPU Cores",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 8"
        })
    )

    pc = forms.FloatField(
        label="Rear Camera (MP)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 12"
        })
    )

    px_height = forms.FloatField(
        label="Screen Pixel Height",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 800"
        })
    )

    px_width = forms.FloatField(
        label="Screen Pixel Width",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 1200"
        })
    )

    ram = forms.FloatField(
        label="RAM (MB)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 4000"
        })
    )

    sc_h = forms.FloatField(
        label="Screen Height (cm)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 15"
        })
    )

    sc_w = forms.FloatField(
        label="Screen Width (cm)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 7"
        })
    )

    talk_time = forms.FloatField(
        label="Talk Time (hours)",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "e.g. 10"
        })
    )

    three_g = forms.ChoiceField(
        label="3G Support",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={"class": "form-select"})
    )

    touch_screen = forms.ChoiceField(
        label="Touch Screen",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={"class": "form-select"})
    )

    wifi = forms.ChoiceField(
        label="WiFi",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.Select(attrs={"class": "form-select"})
    )