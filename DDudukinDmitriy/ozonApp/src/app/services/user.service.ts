import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {UserData} from "../../User";
import {CookieService} from "ngx-cookie-service";


export class UserLogin{
  username:string
  password:string
}
@Injectable({
  providedIn: 'root'
})
export class UserService {
  public isLogin = this.cookieService.get('is_login');
  public token = this.cookieService.get('csrftoken');
  constructor(private http: HttpClient, private cookieService: CookieService) { }

  public registerUser(user){
    this.http.post('/api/register/',{user}).subscribe()
  }
  getUserId(loginAndPassword: UserLogin): Observable<UserLogin>{
    return this.http.post<UserLogin>('/api/login/', loginAndPassword)
  }
  getCustomerData():Observable<UserData>{
    return this.http.get<UserData>('/api/customer/')
  }
  saveEmail(email){
   return this.http.put('/api/customer/',email,{
  headers:new HttpHeaders({
    'X-CSRFToken': this.token
    })
   })
  }
  savePhone(phone){
    return this.http.put('/api/customer/', phone,{
      headers:new HttpHeaders({
        'X-CSRFToken': this.token
      })
    })
  }
  savePersonalData(data) {
    return this.http.put('/api/customer/', data, {
      headers:new HttpHeaders({
        'X-CSRFToken': this.token
      })
    })
  }
  exit(){
    return this.http.get('/api/logout/')
  }
  deleteUser(){
    return this.http.delete('/customer/',{
      headers:new HttpHeaders({
        'X-CSRFToken': this.token
      })
    })
  }
}
