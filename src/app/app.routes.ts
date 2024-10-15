import { Routes } from '@angular/router';
import { ImageComponent } from './image/image.component';  // Import du composant "image"
import { AnalysResultComponent } from './analys-result/analys-result.component';  // Import du composant "analys-result"

export const routes: Routes = [
  { path: '', component: ImageComponent },  // Page d'accueil qui charge "image"
  { path: 'result', component: AnalysResultComponent }  // Page des résultats d'analyse
];
