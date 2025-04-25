import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import CommonModule
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { MatcherService } from '../../services/matcher.service'; // Import the service


@Component({
  selector: 'app-matcher',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './matcher.component.html',
  styleUrls: ['./matcher.component.scss']
})
export class MatcherComponent {
  jobDescription: string = "";
  selectedFiles: File[] = [];
  message: string = "";
  matchedResumes: Array<{ filename: string; similarityScore: number }> = [];

  // Inject MatcherService in the constructor
  constructor(private matcherService: MatcherService) {}

  // Handle multiple file selection
  onFilesChange(event: any): void {
    if (event.target.files && event.target.files.length > 0) {
      this.selectedFiles = Array.from(event.target.files);
    }
  }

  matchResumes(): void {
    if(!this.jobDescription || this.selectedFiles.length === 0) {
      this.message = "Please enter a job description and select at least one resume file."
      return;
    }

    // Call the MatcherService's matchResumes method
    this.matcherService.matchResumes(this.jobDescription, this.selectedFiles).subscribe({
      next: (response) => {
        this.message = "Resumes matched successfully!";
        if (response.top_resumes && response.similarity_scores) {
          this.matchedResumes = response.top_resumes.map((filename: string, index: number) => ({
            filename: filename,
            similarityScore: response.similarity_scores[index]
          }));
        }
      },
      error: (error) => {
        console.error("Error matching resumes", error);
        this.message = "An error occurred while matching resumes.";
      }
    });     
  } 
}


