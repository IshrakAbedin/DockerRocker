FROM mcr.microsoft.com/dotnet/core/sdk:2.1 AS build-env
WORKDIR /app
COPY ./*.sln ./
COPY ./api/*.csproj ./api/
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /out
FROM mcr.microsoft.com/dotnet/core/aspnet:2.1
WORKDIR /app
COPY --from=build-env /out .
ENTRYPOINT dotnet netcore-api.dll
