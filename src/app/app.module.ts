import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { ImageComponent } from './image/image.component';
import { AnalysResultComponent } from './analys-result/analys-result.component';
import { AppRoutingModule } from './app-routing.module';  // Import du module de routage

@NgModule({
  declarations: [
    AppComponent,
    ImageComponent,
    AnalysResultComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule  // Import du module de routage
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
