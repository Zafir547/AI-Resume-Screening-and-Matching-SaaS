import { Component, ViewChild, ElementRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ResumeService } from '../../services/resume.service';


@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './resume.component.html',
  styleUrls: ['./resume.component.scss']
})
export class ResumeComponent {
  @ViewChild('fileInput') fileInput!: ElementRef;

  message: string = '';
  predictedCategory: string = '';
  recommendedJob: string = '';
  name: string = '';
  phone: string = '';
  email: string = '';
  extractedSkills: string[] = [];
  extractedEducation: string[] = [];
  selectedFile: File | null = null;
  
  constructor(private resumeService: ResumeService) {}

  onFileSelected(event: any): void {
    if (event.target.files && event.target.files.length > 0) {
      this.selectedFile = event.target.files[0];
    } else {
      this.selectedFile = null;
    }
  }

  onSubmit(): void {
    if (!this.selectedFile) {
      this.message = 'Please upload a resume file!';
      return;
    }

    // Call the backend API using the resume service
    this.resumeService.uploadResume(this.selectedFile).subscribe({
      next: (response) => {
        // Assuming response returns all neccessary fields
        this.message = 'File uploaded successfully!';
        this.predictedCategory = response.predicted_category;
        this.recommendedJob = response.recommended_job;
        this.name = response.name;
        this.phone = response.phone;
        this.email = response.email;
        this.extractedSkills = response.skills ? response.skills.split(', ') : [];
        this.extractedEducation = response.education ? response.education.split(', ') : [];

        // Reset file input
        this.fileInput.nativeElement.value = '';
        this.selectedFile = null;
      },
      error: (err) => {
        console.error('Error uploading resume', err)
        this.message = 'Error uploading resume. Please try again.'
      }
    });
  }
}
