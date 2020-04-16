import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";


export class User{
  email:string
  password:string
}
@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }
  getUserId(loginAndPassword: User): Observable<User>{
    return this.http.post<User>('/api/login/', loginAndPassword)
  }
}
