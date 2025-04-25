import re
import io
import docx2txt
from typing import List, Optional
from PyPDF2 import PdfReader
from fastapi import UploadFile


async def extract_text_from_upload(file: UploadFile) -> str:
    filename = file.filename.lower()
    file.file.seek(0)
    
    if filename.endswith('.pdf'):
        reader = PdfReader(file.file)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
    
    elif filename.endswith('.docx'):
        content = await file.read()
        text = docx2txt.process(io.BytesIO(content))
    
    elif filename.endswith('.txt'):
        content = await file.read()
        text = content.decode('utf-8')
    
    else:
        return ""

    return text
    
def extract_contact_number(text: str) -> str:
    pattern = r"\+?\d{1,3}[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,5}[-.\s]?\d{4,6}"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_email(text: str) -> str:
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_skills(text: str) -> List[str]:
    skills_list = [
        'Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 'Deep Learning', 'SQL',
        'Tableau', 'Java', 'C++', 'JavaScript', 'HTML', 'CSS', 'React', 'Angular', 'Node.js', 'MongoDB', 'Express.js', 'Git',
        'Research', 'Statistics', 'Quantitative Analysis', 'Qualitative Analysis', 'SPSS', 'R', 'Data Visualization', 'Matplotlib',
        'Seaborn', 'Plotly', 'Pandas', 'Numpy', 'Scikit-learn', 'TensorFlow', 'Keras', 'PyTorch', 'NLTK', 'Text Mining',
        'Natural Language Processing', 'Computer Vision', 'Image Processing', 'OCR', 'Speech Recognition',
        'Recommendation Systems', 'Collaborative Filtering', 'Content-Based Filtering', 'Reinforcement Learning', 'Neural Networks',
        'Convolutional Neural Networks', 'Recurrent Neural Networks', 'Generative Adversarial Networks', 'XGBoost', 'Random Forest',
        'Decision Trees', 'Support Vector Machines', 'Linear Regression', 'Logistic Regression', 'K-Means Clustering',
        'Hierarchical Clustering', 'DBSCAN', 'Association Rule Learning', 'Apache Hadoop', 'Apache Spark', 'MapReduce', 'Hive',
        'HBase', 'Apache Kafka', 'Data Warehousing', 'ETL', 'Big Data Analytics', 'Cloud Computing', 'Amazon Web Services (AWS)',
        'Microsoft Azure', 'Google Cloud Platform (GCP)', 'Docker', 'Kubernetes', 'Linux', 'Shell Scripting', 'Cybersecurity',
        'Network Security', 'Penetration Testing', 'Firewalls', 'Encryption', 'Malware Analysis', 'Digital Forensics', 'CI/CD',
        'DevOps', 'Agile Methodology', 'Scrum', 'Kanban', 'Continuous Integration', 'Continuous Deployment',
        'Software Development', 'Web Development', 'Mobile Development', 'Backend Development', 'Frontend Development',
        'Full-Stack Development', 'UI/UX Design', 'Responsive Design', 'Wireframing', 'Prototyping', 'User Testing',
        'Adobe Creative Suite', 'Photoshop', 'Illustrator', 'InDesign', 'Figma', 'Sketch', 'Zeplin', 'InVision',
        'Product Management', 'Market Research', 'Customer Development', 'Lean Startup', 'Business Development', 'Sales',
        'Marketing', 'Content Marketing', 'Social Media Marketing', 'Email Marketing', 'SEO', 'SEM', 'PPC',
        'Google Analytics', 'Facebook Ads', 'LinkedIn Ads', 'Lead Generation', 'Customer Relationship Management (CRM)',
        'Salesforce', 'HubSpot', 'Zendesk', 'Intercom', 'Customer Support', 'Technical Support', 'Troubleshooting',
        'Ticketing Systems', 'ServiceNow', 'ITIL', 'Quality Assurance', 'Manual Testing', 'Automated Testing', 'Selenium',
        'JUnit', 'Load Testing', 'Performance Testing', 'Regression Testing', 'Black Box Testing', 'White Box Testing',
        'API Testing', 'Mobile Testing', 'Usability Testing', 'Accessibility Testing', 'Cross-Browser Testing',
        'Agile Testing', 'User Acceptance Testing', 'Software Documentation', 'Technical Writing', 'Copywriting',
        'Editing', 'Proofreading', 'Content Management Systems (CMS)', 'WordPress', 'Joomla', 'Drupal', 'Magento',
        'Shopify', 'E-commerce', 'Payment Gateways', 'Inventory Management', 'Supply Chain Management', 'Logistics',
        'Procurement', 'ERP Systems', 'SAP', 'Oracle', 'Microsoft Dynamics', 'Power BI', 'QlikView', 'Looker',
        'Data Engineering', 'Data Governance', 'Data Quality', 'Master Data Management', 'Predictive Analytics',
        'Prescriptive Analytics', 'Descriptive Analytics', 'Business Intelligence', 'Dashboarding', 'Reporting', 'Data Mining',
        'Web Scraping', 'API Integration', 'RESTful APIs', 'GraphQL', 'SOAP', 'Microservices', 'Serverless Architecture',
        'Lambda Functions', 'Event-Driven Architecture', 'Message Queues', 'Socket.io', 'WebSockets', 'Ruby', 'Ruby on Rails',
        'PHP', 'Symfony', 'Laravel', 'CakePHP', 'Zend Framework', 'ASP.NET', 'C#', 'VB.NET', 'ASP.NET MVC', 'Entity Framework',
        'Spring', 'Hibernate', 'Struts', 'Kotlin', 'Swift', 'Objective-C', 'iOS Development', 'Android Development', 'Flutter',
        'React Native', 'Ionic', 'Mobile UI/UX Design', 'Material Design', 'SwiftUI', 'RxJava', 'RxSwift', 'Django', 'Flask',
        'FastAPI', 'Falcon', 'Tornado', 'RESTful Web Services', 'Microservices Architecture', 'Serverless Computing',
        'AWS Lambda', 'Google Cloud Functions', 'Azure Functions', 'Server Administration', 'System Administration',
        'Network Administration', 'Database Administration', 'MySQL', 'PostgreSQL', 'SQLite', 'Microsoft SQL Server',
        'Oracle Database', 'NoSQL', 'MongoDB', 'Cassandra', 'Redis', 'Elasticsearch', 'Firebase', 'Google Tag Manager',
        'Adobe Analytics', 'Marketing Automation', 'Customer Data Platforms', 'Segment', 'Salesforce Marketing Cloud',
        'HubSpot CRM', 'Zapier', 'IFTTT', 'Workflow Automation', 'Robotic Process Automation (RPA)', 'UI Automation',
        'Natural Language Generation (NLG)', 'Virtual Reality (VR)', 'Augmented Reality (AR)', 'Mixed Reality (MR)',
        'Unity', 'Unreal Engine', '3D Modeling', 'Animation', 'Motion Graphics', 'Game Design', 'Game Development',
        'Level Design', 'Unity3D', 'Unreal Engine 4', 'Blender', 'Maya', 'Adobe After Effects', 'Adobe Premiere Pro',
        'Final Cut Pro', 'Video Editing', 'Audio Editing', 'Sound Design', 'Music Production', 'Digital Marketing',
        'Content Strategy', 'Conversion Rate Optimization (CRO)', 'A/B Testing', 'Customer Experience (CX)',
        'User Experience (UX)', 'User Interface (UI)', 'Persona Development', 'User Journey Mapping',
        'Information Architecture (IA)', 'Wireframing', 'Prototyping', 'Usability Testing', 'Accessibility Compliance',
        'Internationalization (I18n)', 'Localization (L10n)', 'Voice User Interface (VUI)', 'Chatbots',
        'Natural Language Understanding (NLU)', 'Speech Synthesis', 'Emotion Detection', 'Sentiment Analysis',
        'Image Recognition', 'Object Detection', 'Facial Recognition', 'Gesture Recognition', 'Document Recognition',
        'Fraud Detection', 'Cyber Threat Intelligence', 'Security Information and Event Management (SIEM)',
        'Vulnerability Assessment', 'Incident Response', 'Forensic Analysis', 'Security Operations Center (SOC)',
        'Identity and Access Management (IAM)', 'Single Sign-On (SSO)', 'Multi-Factor Authentication (MFA)',
        'Blockchain', 'Cryptocurrency', 'Decentralized Finance (DeFi)', 'Smart Contracts', 'Web3',
        'Non-Fungible Tokens (NFTs)'
    ]
    skills = []
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        if re.search(pattern, text, re.IGNORECASE):
            skills.append(skill)
    return skills


def extract_education(text: str) -> List[str]:
    education_keywords = [
        'Computer Science', 'Information Technology', 'Software Engineering', 'Electrical Engineering', 'Mechanical Engineering',
        'Civil Engineering', 'Chemical Engineering', 'Biomedical Engineering', 'Aerospace Engineering', 'Nuclear Engineering',
        'Industrial Engineering', 'Systems Engineering', 'Environmental Engineering', 'Petroleum Engineering',
        'Geological Engineering', 'Marine Engineering', 'Robotics Engineering', 'Biotechnology', 'Biochemistry',
        'Microbiology', 'Genetics', 'Molecular Biology', 'Bioinformatics', 'Neuroscience', 'Biophysics', 'Biostatistics',
        'Pharmacology', 'Physiology', 'Anatomy', 'Pathology', 'Immunology', 'Epidemiology', 'Public Health',
        'Health Administration', 'Nursing', 'Medicine', 'Dentistry', 'Pharmacy', 'Veterinary Medicine', 'Medical Technology',
        'Radiography', 'Physical Therapy', 'Occupational Therapy', 'Speech Therapy', 'Nutrition', 'Sports Science',
        'Kinesiology', 'Exercise Physiology', 'Sports Medicine', 'Rehabilitation Science', 'Psychology', 'Counseling',
        'Social Work', 'Sociology', 'Anthropology', 'Criminal Justice', 'Political Science', 'International Relations',
        'Economics', 'Finance', 'Accounting', 'Business Administration', 'Management', 'Marketing', 'Entrepreneurship',
        'Hospitality Management', 'Tourism Management', 'Supply Chain Management', 'Logistics Management',
        'Operations Management', 'Human Resource Management', 'Organizational Behavior', 'Project Management',
        'Quality Management', 'Risk Management', 'Strategic Management', 'Public Administration', 'Urban Planning',
        'Architecture', 'Interior Design', 'Landscape Architecture', 'Fine Arts', 'Visual Arts', 'Graphic Design',
        'Fashion Design', 'Industrial Design', 'Product Design', 'Animation', 'Film Studies', 'Media Studies',
        'Communication Studies', 'Journalism', 'Broadcasting', 'Creative Writing', 'English Literature', 'Linguistics',
        'Translation Studies', 'Foreign Languages', 'Modern Languages', 'Classical Studies', 'History', 'Archaeology',
        'Philosophy', 'Theology', 'Religious Studies', 'Ethics', 'Education', 'Early Childhood Education',
        'Elementary Education', 'Secondary Education', 'Special Education', 'Higher Education', 'Adult Education',
        'Distance Education', 'Online Education', 'Instructional Design', 'Curriculum Development',
        'Library Science', 'Information Science', 'Computer Engineering', 'Software Development', 'Cybersecurity',
        'Information Security', 'Network Engineering', 'Data Science', 'Data Analytics', 'Business Analytics',
        'Operations Research', 'Decision Sciences', 'Human-Computer Interaction', 'User Experience Design',
        'User Interface Design', 'Digital Marketing', 'Content Strategy', 'Brand Management', 'Public Relations',
        'Corporate Communications', 'Media Production', 'Digital Media'
    ]
    education = []
    for keyword in education_keywords:
        pattern = r"(?i)\b{}\b".format(re.escape(keyword))
        match = re.search(pattern, text)
        if match:
            education.append(match.group())
    return education

def extract_name(text: str) -> Optional[str]:
    """Extract name from the resume. It assumes the first non-empty line is the name."""
    lines = text.split("\n")
    
    for line in lines:
        line = line.strip()
        
        # Ignore empty lines and common words
        if not line or any(word in line.lower() for word in ["summary", "contact", "experience", "skills", "linkedin"]):
            continue
        
        # Extract potential name (first two words)
        match = re.match(r"([A-Z][a-zA-Z]+)\s+([A-Z][a-zA-Z]+)", line)
        if match:
            return match.group()
    
    return "Unknown Name"
