import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Archivo } from '../models/Archivo';
@Injectable({
  providedIn: 'root'
})
export class UserService {

  API = 'http://localhost:3000';


  constructor(private http:HttpClient) { }

  ejecutar(archivo: Archivo|JSON){
    return this.http.post(`${this.API}/ejecutar`, archivo);
  }

  getConsola(){
    return this.http.get(`${this.API}/consola`);
  }
}
