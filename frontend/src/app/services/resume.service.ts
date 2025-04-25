import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn: "root"
})
export class ResumeService {
    // Use your backend URL (adjust if using proxy)
    private baseUrl = 'http://localhost:8000';

    constructor(private http: HttpClient) {}

    uploadResume(file: File): Observable<any> {
        const formData = new FormData();
        formData.append("resume", file);
        return this.http.post(`${this.baseUrl}/api/predict_resume`, formData);
    }
}