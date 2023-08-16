import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddUsersComponent } from './add-users/add-users.component';
import { ListUsersComponent } from './list-users/list-users.component';
import { EditUsersComponent } from './edit-users/edit-users.component';
import { ReactiveFormsModule } from '@angular/forms';
import { AddProductsComponent } from './add-products/add-products.component';
import { EditProductsComponent } from './edit-products/edit-products.component';
import { ListProductsComponent } from './list-products/list-products.component';
import { EditSerialsComponent } from './edit-serials/edit-serials.component'; 
import { ListSerialsComponent } from './list-serials/list-serials.component'; 
import { AddSerialsComponent } from './add-serials/add-serials.component'; 
import { BoardAdminComponent } from './board-admin/board-admin.component';
import { BoardModeratorComponent } from './board-moderator/board-moderator.component';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { KeyCSRListComponent } from './key-csr-list/key-csr-list.component';
import { AddCsrComponent } from './add-csr/add-csr.component';
import { EditCsrComponent } from './edit-csr/edit-csr.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import {  HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuthenticationService } from './authentication.service';
import { SerialService } from './serial.service';
import { FormsModule } from '@angular/forms';
import { DataService } from './data.service'; 
import { EventBusService } from './event-bus.service';
import { KeyCSRService } from './key-csr.service';
import { StorageService } from './storage.service';
import { AuthGuardService } from './auth-guard.service';
import { UpdateProfileComponent } from './update-profile/update-profile.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { PasswordresetComponent } from './passwordreset/passwordreset.component';
import { PasswordResetFormComponent } from './password-reset-form/password-reset-form.component';
import { ChangePasswordComponent } from './change-password/change-password.component';
import { UserService } from './user.service';
import { ProductsService } from './products.service';
import {HttpRequestInterceptor, httpInterceptorProviders } from './http.interceptor';
import { JwtHelperService, JWT_OPTIONS } from '@auth0/angular-jwt';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from '@angular/material/dialog';
import { DeleteDialogSerialComponent } from './delete-dialog-serial/delete-dialog-serial.component';
import { DeleteDialogProductComponent } from './delete-dialog-product/delete-dialog-product.component';

@NgModule({
  declarations: [
    AppComponent,
    PasswordresetComponent,
    AddUsersComponent,
    ListUsersComponent,
    EditUsersComponent,
    AddProductsComponent,
    EditProductsComponent,
    ListProductsComponent,
    EditSerialsComponent,
    ListSerialsComponent,
    AddSerialsComponent,
    BoardAdminComponent ,
    BoardModeratorComponent,
    ProfileComponent,
    HomeComponent ,
    LoginComponent,
    AddCsrComponent,
    KeyCSRListComponent,
    EditCsrComponent ,
    SignupComponent,
    UpdateProfileComponent,
    ResetPasswordComponent,
    PasswordResetFormComponent,
    ChangePasswordComponent,
    DeleteDialogSerialComponent,
    DeleteDialogProductComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    MatDialogModule
    
  ],
  providers: [
     httpInterceptorProviders,
     { provide: JWT_OPTIONS, useValue: JWT_OPTIONS },
    JwtHelperService

    
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
