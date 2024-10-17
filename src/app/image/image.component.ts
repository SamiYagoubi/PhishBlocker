import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-image',
  templateUrl: './image.component.html',
  styleUrls: ['./image.component.css']
})
export class ImageComponent {
  selectedFile: File | null = null;

  constructor(private http: HttpClient, private router: Router) { }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length) {
      this.selectedFile = input.files[0];
    }
  }

  onUpload(): void {
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('file', this.selectedFile, this.selectedFile.name);

      // Envoi de l'image au backend pour analyse
      this.http.post('URL_DU_BACKEND_POUR_ANALYSE', formData)
        .subscribe(response => {
          this.router.navigate(['/result'], { state: { data: response } });  // Redirection vers la page des résultats
        });
    }
  }
}
