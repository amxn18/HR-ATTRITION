from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated

class EmployeeFeatures(BaseModel):
    # Demographics 
    Age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=100,
            description="Age of the employee"
        )
    ]

    Gender: Annotated[
        Literal["Male", "Female"],
        Field(
            ...,
            description="Gender of the employee"
        )
    ]

    MaritalStatus: Annotated[
        Literal["Single", "Married", "Divorced"],
        Field(
            ...,
            description="Marital status of the employee"
        )
    ]

    # Job & Role 
    Department: Annotated[
        Literal["Sales", "Research & Development", "Human Resources"],
        Field(
            ...,
            description="Department of the employee",
            examples=["Sales"]
        )
    ]

    JobRole: Annotated[
        str,
        Field(
            ...,
            description="Job role of the employee",
            examples=["Sales Executive"]
        )
    ]

    JobLevel: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=5,
            description="Job level (1–5)",
            examples=[2]
        )
    ]

    JobInvolvement: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=4,
            description="Job involvement score (1–4)",
            examples=[3]
        )
    ]

    # Compensation 
    MonthlyIncome: Annotated[
        int,
        Field(
            ...,
            gt=0,
            description="Monthly income of the employee",
            examples=[5000]
        )
    ]

    PercentSalaryHike: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=100,
            description="Percentage salary hike",
            examples=[12]
        )
    ]

    StockOptionLevel: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=3,
            description="Stock option level",
            examples=[1]
        )
    ]

    # Work Conditions 
    BusinessTravel: Annotated[
        Literal["Travel_Rarely", "Travel_Frequently", "Non-Travel"],
        Field(
            ...,
            description="Frequency of business travel",
            examples=["Travel_Rarely"]
        )
    ]

    DistanceFromHome: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="Distance from home in kilometers",
            examples=[5]
        )
    ]

    OverTime: Annotated[
        Literal["Yes", "No"],
        Field(
            ...,
            description="Does the employee work overtime?",
            examples=["Yes"]
        )
    ]

    WorkLifeBalance: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=4,
            description="Work-life balance score (1–4)",
            examples=[3]
        )
    ]

    # Satisfaction & Performance 
    JobSatisfaction: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=4,
            description="Job satisfaction score (1–4)",
            examples=[3]
        )
    ]

    EnvironmentSatisfaction: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=4,
            description="Environment satisfaction score (1–4)",
            examples=[3]
        )
    ]

    RelationshipSatisfaction: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=4,
            description="Relationship satisfaction score (1–4)",
            examples=[2]
        )
    ]

    PerformanceRating: Annotated[
        int,
        Field(
            ...,
            ge=1,
            le=4,
            description="Performance rating (1–4)",
            examples=[3]
        )
    ]

    # Experience
    TotalWorkingYears: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="Total working experience in years",
            examples=[10]
        )
    ]

    YearsAtCompany: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="Years spent at the company",
            examples=[5]
        )
    ]

    YearsInCurrentRole: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="Years in current role",
            examples=[3]
        )
    ]

    YearsSinceLastPromotion: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="Years since last promotion",
            examples=[2]
        )
    ]

    YearsWithCurrManager: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="Years with current manager",
            examples=[3]
        )
    ]

    # Rates 
    DailyRate: Annotated[int, Field(..., gt=0, examples=[1100])]
    HourlyRate: Annotated[int, Field(..., gt=0, examples=[60])]
    MonthlyRate: Annotated[int, Field(..., gt=0, examples=[20000])]
    NumCompaniesWorked: Annotated[int, Field(..., ge=0, examples=[2])]
    Education: Annotated[int, Field(..., ge=1, le=5, examples=[3])]
    EducationField: Annotated[str, Field(..., examples=["Life Sciences"])]
    TrainingTimesLastYear: Annotated[int, Field(..., ge=0, examples=[3])]

    # Normalization
    @field_validator("EducationField", "JobRole", "Department")
    @classmethod
    def normalize_strings(cls, v: str) -> str:
        return v.strip()
