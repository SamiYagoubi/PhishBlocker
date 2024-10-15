import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { routes } from './app.routes';  // Import des routes définies dans app.routes.ts

@NgModule({
  imports: [RouterModule.forRoot(routes)],  // Utilisation des routes dans l'application
  exports: [RouterModule]  // Export du RouterModule pour qu'il soit disponible dans l'application
})
export class AppRoutingModule { }
