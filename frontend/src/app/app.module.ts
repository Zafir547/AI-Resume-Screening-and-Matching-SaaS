// import { BrowserModule } from '@angular/platform-browser';
// import { NgModule } from '@angular/core';
// import { HttpClientModule } from '@angular/common/http';
// import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// import { AppRoutingModule } from './app-routing.module';
// import { AppComponent } from './app.component';
// import { ResumeComponent } from './components/resume/resume.component';
// import { MatcherComponent } from './components/matcher/matcher.component';

// @NgModule({
//   declarations: [
//     AppComponent,
//     ResumeComponent,
//     MatcherComponent
//   ],
//   imports: [
//     BrowserModule,
//     HttpClientModule,
//     FormsModule,
//     ReactiveFormsModule,
//     AppRoutingModule
//   ],
//   providers: [],
//   bootstrap: [AppComponent]
// })
// export class AppModule { }

// import { NgModule } from '@angular/core';
// import { BrowserModule } from '@angular/platform-browser';
// import { AppComponent } from './app.component';
// import { HeaderComponent } from './components/header/header.component';
// import { MatcherComponent } from './components/matcher/matcher.component';
// import { ResumeComponent } from './components/resume/resume.component';
// import { RouterModule } from '@angular/router';

// @NgModule({
//   declarations: [  // ✅ Declare components here if they are NOT standalone
//     AppComponent,
//     HeaderComponent,
//     MatcherComponent,
//     ResumeComponent
//   ],
//   imports: [
//     BrowserModule,
//     RouterModule
//   ],
//   providers: [],
//   bootstrap: [AppComponent]
// })
// export class AppModule { }


import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common'; // Import this
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { MatcherComponent } from './components/matcher/matcher.component';
import { ResumeComponent } from './components/resume/resume.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    MatcherComponent,
    ResumeComponent
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    CommonModule,
    RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }


