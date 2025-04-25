import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { MatcherComponent } from './components/matcher/matcher.component';
import { ResumeComponent } from './components/resume/resume.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent,ResumeComponent, MatcherComponent,],
  // imports: [RouterOutlet, HeaderComponent, ResumeComponent],  

  template: `
    <!-- <h1>Welocme to {{title}}</h1> -->
    
    <app-header />
    <app-matcher />
    <app-resume />
    <router-outlet />
    
    
  `,
  styles: []
})
export class AppComponent {
  title = 'AI Resume Screening and Job Matching';
}