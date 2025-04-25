import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ResumeComponent } from './components/resume/resume.component';
import { MatcherComponent } from './components/matcher/matcher.component';

const routes: Routes = [
  { path: 'resume', component: ResumeComponent },
  { path: 'matcher', component: MatcherComponent },
  { path: '', redirectTo: '/resume', pathMatch: 'full' },
  { path: '**', redirectTo: '/resume' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

