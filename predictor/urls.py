from django.urls import path
from . import views

urlpatterns = [
    path("", views.predict_price_view, name="predict"),
    path("dashboard/", views.history_view, name="dashboard"),

    # View Prediction Details
    path("view/<int:id>/", views.view_prediction, name="view_prediction"),

    # Update Prediction
    path("update/<int:id>/", views.update_prediction, name="update"),

    # Delete Prediction
    path("delete/<int:id>/", views.delete_prediction, name="delete"),

    # Export CSV
    path("export/csv/", views.export_csv, name="export_csv"),
]