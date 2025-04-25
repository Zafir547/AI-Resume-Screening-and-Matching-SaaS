import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn: "root"
})
export class MatcherService {
    private baseUrl = 'http://localhost:8000';

    constructor(private http: HttpClient) {}

    matchResumes(jobDescription: string, files: File[]): Observable<any> {
        const formData = new FormData();
        formData.append("job_description", jobDescription);
        files.forEach(file => {
            formData.append("resumes", file);
        });
        // Updated URL to match backend endpoint
        return this.http.post(`${this.baseUrl}/api/match_resumes`, formData);
    }
}
