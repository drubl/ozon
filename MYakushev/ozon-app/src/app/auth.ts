import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

export class AuthId {
  id = 0;
}

@Injectable({
  providedIn: 'root'
})
export class Auth {
  private logInUrl = '/api/login/';
  constructor(private http: HttpClient) { }
  public id: number;
  login(loginCustomer)  {
    console.log(loginCustomer);
    this.http.post<AuthId>(this.logInUrl, loginCustomer).subscribe(answer => {
      this.id = answer.id;
    });
    return this.http.post<AuthId>(this.logInUrl, loginCustomer);
  }
  logout() {
  }
}
